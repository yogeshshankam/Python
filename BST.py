class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_valid_bst(node, left=float('-inf'), right=float('inf')):
    # An empty tree is considered a valid BST
    if node is None:
        return True
    
    # The current node's value must be within the defined range
    if not (left < node.value < right):
        return False
    
    # Recursively validate the left and right subtrees
    return (is_valid_bst(node.left, left, node.value) and
            is_valid_bst(node.right, node.value, right))

# Example usage:
# Constructing a simple BST
#       2
#      / \
#     1   3
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(is_valid_bst(root))  # Output: True

# Example usage:
# Constructing a simple BST
#       2
#      / \
#     1   0
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(0)

print(is_valid_bst(root))  # Output: False
