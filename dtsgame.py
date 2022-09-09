# DTS Memory Game Assignment

import pygame
#implement pygame-gui
import random
import os

pygame.init()



# Game Variables & Constants
WIDTH = 600
HEIGHT = 600
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
gray = (128, 128, 128)
#I have created and set my game variables and constatnts and labeled them for easy access

fps = 60
#Locked fps to 60 as unlocked fps caused screen tearing

timer = pygame.time.Clock()
rows = 6
cols = 8

correct = [[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0]]

#more constants/varables

options_list = []
spaces = []
used = []
new_board = True
first_guess = False
second_guess = False
first_guess_num = 0
second_guess_num = 0
score = 0
best_score = 0
matches = 0
game_over = False

HS_file = "best_score.txt" #file
dir = os.path.join("C:\\", "temp") #directory

# defines load data (loads data read off of hsfile)
def load_data():

   with open(os.path.join(dir, HS_file), 'r') as f:
       try:
           best_score = int(f.read())
           return best_score
       except:
           best_score = 0
           return best_score
       best_score = str(load_data())  # set variable score into loaded data from file



#Set more constants and variables for easy access

# Screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Memory Game by Muhammad")
title_font = pygame.font.SysFont('freesansbold', 100)
small_font = pygame.font.SysFont('freesansbold', 40)
restart_font = pygame.font.SysFont('freesansbold', 80)
winner_font = pygame.font.SysFont('freesansbold', 50)
#Created my font to be easily read and set size to a good fit in the game

#board
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
    restart_button = pygame.draw.rect(screen, gray, [10, HEIGHT - 90, 200, 80], 0, 5)
    restart_text = restart_font.render('Restart', True, white)
    screen.blit(restart_text, (10, 520))
    score_text = small_font.render(f'Current Turns: {score}', True, white)
    screen.blit(score_text, (350, 520))
    best_text = small_font.render(f'High Score: {best_score}', True, white)
    screen.blit(best_text, (350, 560))
    return restart_button

#Buttons and Texts are set to their final design for the game and displayed through these codes.

#board functions
def draw_board():
    global rows
    global cols
    global correct
    board_list = []
    for y in range(cols):
        for x in range(rows):
            piece = pygame.draw.rect(screen, white, [y * 75 + 12, x * 65 + 112, 50, 50], 0, 4)
            board_list.append(piece)

            piece_text = small_font.render(f'{spaces[y * rows + x]}', True, gray)
            screen.blit(piece_text, (y * 75 + 18, x * 65 + 120))

            #lines above are hiding the game answers, when the # is removed the correct numbers appear on screen


    for r in range(rows):
        for c in range(cols):
            if correct[r][c] == 1:
                pygame.draw.rect(screen, green, [c * 75 + 10, r * 65 + 110, 54, 54], 3, 4)
                piece_text = small_font.render(f'{spaces[c * rows + r]}', True, black)
                screen.blit(piece_text, (c * 75 + 18, r * 65 + 120))
    return board_list

#guesses
def check_guesses(first, second):
    global spaces
    global correct
    global score
    global matches
    if spaces[first] == spaces[second]:
        col1 = first // rows
        col2 = second // rows
        row1 = first - (col1 * rows)
        row2 = second - (col2 * rows)
        if correct[row1][col1] == 0 and correct[row2][col2] == 0:
            correct[row1][col1] = 1
            correct[row2][col2] = 1
            score += 1
            matches += 1

    else:
        score += 1
#This checks the board for guesses made by the player and verifies the guesses to create the score and show current turns

running = True
while running:
    timer.tick(fps)
    screen.fill(white)

    # checks to see if file and directory exist if they do not it will make them
    isexists = os.path.exists(dir)
    file_exist = os.path.exists(os.path.join(dir, HS_file))
    if not isexists:
        os.makedirs(dir, exist_ok=False)
    if not file_exist:
        open(os.path.join(dir, HS_file), 'w')

    if new_board:
        generate_board()
        new_board = False

    restart = draw_backgrounds()
    board = draw_board()

    load_data()

#Answer Delay
    if first_guess and second_guess:
        check_guesses(first_guess_num, second_guess_num)
        pygame.time.delay(1000)
        first_guess = False
        second_guess = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type ==  pygame.MOUSEBUTTONDOWN:
            for i in range(len(board)):
                button = board[i]
                if not game_over:
                   if button.collidepoint(event.pos) and not first_guess:
                       first_guess = True
                       first_guess_num = i
                   if button.collidepoint(event.pos) and not second_guess and first_guess and i != first_guess_num:
                        second_guess = True
                        second_guess_num = i
            if restart.collidepoint(event.pos):
                options_list = []
                used = []
                spaces = []
                new_board = True
                score = 0
                matches = 0
                first_guess = False
                second_guess = False
                correct = [[0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0]]
                game_over = False

#Creating a restart button if the player desires to start the game over again.

    if matches == rows * cols // 2:
        game_over = True
        winner = pygame.draw.rect(screen, gray, [10, HEIGHT - 300, WIDTH - 20, 80], 0, 5)
        winner_text = winner_font.render(f'Congrats Sir You Won in {score} Turns!', True, white)
        screen.blit(winner_text, (10, HEIGHT - 290))

        if best_score > score or best_score == 0:
           best_score = score
    ("best_score: ", best_score)
                # write_2_file()
    with open(os.path.join(dir, HS_file), 'w') as f:
        f.write(str(best_score))
    ('start writing to file')
    f.close()


    if first_guess:
        piece_text = small_font.render(f'{spaces[first_guess_num]}', True, blue)
        location = (first_guess_num // rows * 75 + 18, (first_guess_num - (first_guess_num // rows * rows)) * 65 + 120)
        screen.blit(piece_text, (location))

    if second_guess:
        piece_text = small_font.render(f'{spaces[second_guess_num]}', True, blue)
        location = (second_guess_num // rows * 75 + 18, (second_guess_num - (second_guess_num // rows * rows)) * 65 + 120)
        screen.blit(piece_text, (location))


    pygame.display.flip()
pygame.quit()