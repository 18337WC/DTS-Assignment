# Memory Game
import pygame
import pygame_gui

pygame.init()

pygame.display.set_caption("Memory Game By Muhammad")
pygame.display.flip()
manager = pygame_gui.UIManager((800, 600))

x = 50
y = 50
width = 40
height = 60
velocity = 5

is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    pygame.display.update()

pygame.quit()

BANNANA = "bannana"
APPLE = "apple"
CARROT = "carrot"
ORANGE = "orange"
