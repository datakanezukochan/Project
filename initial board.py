# this is the code for initial board

import pygame
import sys
import os
import speech_recognition as sr

# Initializing Pygame
pygame.init()
 
def initial_board():
    # Set up the display
    board = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Hangmans game')

    # Defining colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with white
        board.fill(WHITE)
        # DRAWING THE HANGING ROPE
        # Drawing a vertical line
        pygame.draw.line(board, BLACK, (400, 100), (400, 300), 5)
        # Drawing the bottom horizontal line
        pygame.draw.line(board, BLACK, (350,300), (450,300), 5)
        # Drawing the upper horizontal line
        pygame.draw.line(board, BLACK, (300,100), (400,100), 5)
        # Drawing the smaller vertical line
        pygame.draw.line(board, BLACK, (300, 100), (300, 150), 5)

        # # GETTING BUTTONS ON SCREEN
        # class button():
        #     # deciding colors for button
        #     button_color = (25,190,255)
        #     text_color = (0,0,0)
        #     # deciding dimensions of button
        #     width = 180
        #     height = 40
        #     # coding buttons
        #     def __init__(self, x, y, text):
        #         self.x = x
        #         self.y = y
        #         self.text = text
        #     def draw_button (self):
        #         # getting the postion of mouse
        #         position = pygame.mouse.get_pos()

        #         # drawing a button
        #         button_circle = pygame.draw.circle(board, BLACK, (300,220), 5)

        #         # setting condition for which when button will be on the same position as we will do some action
        #         if button_circle.collidepoint(position):


     
        # Update the display
        pygame.display.flip()

    

initial_board()

