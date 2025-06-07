import pygame

 
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BAR_HEIGHT = 20
MARGIN = 30
 
def draw_tree(root, screen, x, y, branch_length=100):
  pygame.draw.rect(screen, WHITE, (x, y, branch_length, BAR_HEIGHT))
  pygame.draw.line(screen, GREEN, (x + branch_length, y + BAR_HEIGHT // 2),
                             (x + branch_length + branch_length // 2, y + BAR_HEIGHT // 2), 3)

  for child in root['children']:
   new_x = x + branch_length + MARGIN
   draw_tree(child, screen, new_x, y + BAR_HEIGHT // 2, branch_length=branch_length // 2, )

pygame.init()
size = (600, 400)
screen = pygame.display.set_mode(size)
pyigame.display.set_caption("Tree Structure")
 
# Example tree data
tree = {
  'name': 'Root',
  'children': [
  {'name': 'Branch 1', 'children': [{'name': 'Leaf 1.1', 'children': []}]},
  {'name': 'Branch 2', 'children': [{'name': 'Leaf 2.1', 'children': []},  
        {'name': 'Leaf 2.2', 'children': []}]},
  ]
}
  
background = pygame.Surface(size)
background.fill((0, 0, 0))
screen.blit(background, (0, 0))
draw_tree(tree, screen, 50, 100)  
pygame.display.flip()
  
running = True
while running:
   for event in pygame.event.get():
     if event.type == pygame.QUIT:
       running = False
   pygame.display.update()
