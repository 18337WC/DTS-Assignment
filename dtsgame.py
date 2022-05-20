import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
white = [255, 255, 255]
red = [255, 0, 0]
screen.fill(white)
pygame.display.set_caption("Memory Game By Muhammad")
pygame.display.flip()

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

