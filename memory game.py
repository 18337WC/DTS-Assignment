# DTS Memory Game Assignment
import random

import pygame

pygame.init()

# Game Variables & Constants
WIDTH = 600
HEIGHT = 600
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)

fps = 60
timer = pygame.time.Clock()
rows = 6
cols = 8
correct = []
options_list = []
spaces = []
used = []
new_board = True

# Screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Memory Game by Muhammad")
title_font = pygame.font.SysFont('freesansbold', 100)
small_font = pygame.font.SysFont('freesansbold', 26)


def generate_board():
    global options_list
    global spaces
    global used
    for item in range(rows * cols // 2):
        options_list.append(item)

    for item in range(rows * cols):
        piece = options_list[random.randint(0, len(options_list)-1)]
        spaces.append(piece)
        if piece in used:
            used.remove(piece)
            options_list.remove(piece)
        else:
            used.append(piece)



def draw_backgrounds():
    top_menu = pygame.draw.rect(screen, black, [0, 0, WIDTH, 100])
    title_text = title_font.render('Memory Game', True, white)
    screen.blit(title_text, (65, 15))
    board_space = pygame.draw.rect(screen, gray, [0, 100, WIDTH, HEIGHT - 200])
    bottom_menu = pygame.draw.rect(screen, black, [0, HEIGHT - 100, WIDTH, 100])


def draw_board():
    global rows
    global cols
    board_list = []
    for y in range(cols):
        for x in range(rows):
            piece = pygame.draw.rect(screen, white, [y * 75 + 12, x * 65 + 112, 50, 50], 0, 4)
            board_list.append(piece)
            piece_text = small_font.render(f'{spaces[y * rows + x]}', True, gray)
            screen.blit(piece_text, (y * 75 + 18, x * 65 + 120))
    return board_list


running = True
while running:
    timer.tick(fps)
    screen.fill(white)
    if new_board:
        generate_board()
        print(spaces)
        new_board = False

    draw_backgrounds()
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()
