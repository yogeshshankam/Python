import time
import win32com.client
import win32gui
import win32con

DISCORD_APP_NAME = "Discord"

def is_discord_open():
    return win32gui.FindWindow(None, DISCORD_APP_NAME) > 0

def find_discord_message_list_hwnd():
    """
    Find the handle of the 'Messages' list in the active Discord channel.
    It's assumed to be the first child window of the Channel Details window.
    """
    discord_hwnd = win32gui.FindWindow(None, DISCORD_APP_NAME)
    channel_details_hwnd = win32gui.GetWindow(discord_hwnd, win32con.GW_CHILD)
    message_list_hwnd = win32gui.GetWindow(channel_details_hwnd, win32con.GW_CHILD)
    return message_list_hwnd

def right_click_message(message_hwnd):
    # Calculate the center of the message element
    rect = win32gui.GetWindowRect(message_hwnd)
    x_center = (rect[2] + rect[0]) // 2
    y_center = (rect[3] + rect[1]) // 2

    # Perform a right-click at the calculated position
    win32api.SetCursorPos((x_center, y_center))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x_center, y_center, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x_center, y_center, 0, 0)

    time.sleep(0.1)  # Small delay for the menu to appear

def click_delete_message():
    # Discord uses a standard menu item ID for 'Delete', we can use it to find the handle
    delete_menu_item_id = 0xF100
    discord_hwnd = win32gui.FindWindow(None, DISCORD_APP_NAME)
    delete_menu_hwnd = win32gui.FindWindowEx(discord_hwnd, 0, "AfxControlBar70", None)
    win32gui.PostMessage(delete_menu_hwnd, win32con.WM_COMMAND, delete_menu_item_id, 0)

def main():
    if not is_discord_open():
        print("Discord is not open.")
        return

    message_list_hwnd = find_discord_message_list_hwnd()
    if not message_list_hwnd:  
        print("Couldn't find the 'Messages' list window.")
        return

    #TODO: Implement logic to find the correct message to delete
    # For now, let's just delete the top message:
    first_message_hwnd = win32gui.GetWindow(message_list_hwnd, win32con.GW_CHILD)

    right_click_message(first_message_hwnd)
    time.sleep(0.5)  # delay for the right-click menu to appear
    click_delete_message()
    
    time.sleep(1)  # Delay for the confirmation dialog to appear

    # Confirm delete by clicking the "Delete" button in the popup dialog
    delete_button_hwnd = win32gui.FindWindowEx(None, None, "Button", "Delete")
    win32gui.SendMessage(delete_button_hwnd, win32con.BM_CLICK, 0, 0)

if __name__ == "__main__":
    main()
