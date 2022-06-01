# Memory Game
import pygame
import random
import pygame_gui

pygame.init()
manager = pygame_gui.UIManager((800, 600))
surface = pygame.display.set_mode((800,600))
color = (0, 0, 0)
surface.fill(color)
pygame.display.flip()

pygame.display.set_caption("Memory Game By Muhammad")
pygame.display.flip()

x = 50
y = 50
width = 40
height = 60
velocity = 5

surface = pygame.display.set_mode((800,600))
color = (255,255,255)
pygame.draw.rect(surface, color, pygame.Rect(200, 200, 80, 80), 2)
pygame.display.flip()

pygame.draw.rect(surface, color, pygame.Rect(300, 200, 80, 80), 2)
pygame.draw.rect(surface, color, pygame.Rect(400, 200, 80, 80), 2)
pygame.draw.rect(surface, color, pygame.Rect(500, 200, 80, 80), 2)
pygame.draw.rect(surface, color, pygame.Rect(200, 300, 80, 80), 2)
pygame.draw.rect(surface, color, pygame.Rect(300, 300, 80, 80), 2)
pygame.draw.rect(surface, color, pygame.Rect(400, 300, 80, 80), 2)
pygame.draw.rect(surface, color, pygame.Rect(500, 300, 80, 80), 2)
pygame.draw.rect(surface, color, pygame.Rect(200, 100, 80, 80), 2)
pygame.draw.rect(surface, color, pygame.Rect(300, 100, 80, 80), 2)
pygame.draw.rect(surface, color, pygame.Rect(400, 100, 80, 80), 2)
pygame.draw.rect(surface, color, pygame.Rect(500, 100, 80, 80), 2)
pygame.draw.rect(surface, color, pygame.Rect(200, 400, 80, 80), 2)
pygame.draw.rect(surface, color, pygame.Rect(300, 400, 80, 80), 2)
pygame.draw.rect(surface, color, pygame.Rect(400, 400, 80, 80), 2)
pygame.draw.rect(surface, color, pygame.Rect(500, 400, 80, 80), 2)

myfont = pygame.font.SysFont("monospace", 50)
WHITE = (255, 255, 255)
label = myfont.render("Memory Game", 1, WHITE)
surface.blit(label, (225, 25))

myfont = pygame.font.SysFont("monospace", 20)
WHITE = (255, 255, 255)
label = myfont.render("banana", 1, WHITE)
surface.blit(label, (204, 126))




is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    pygame.display.update()

pygame.quit()