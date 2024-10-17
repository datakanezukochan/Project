# this is the code for initial board

import pygame
import sys
import os
# import speech_recognition as sr

# Initializing Pygame
clicked = False
pygame.init()
def initial_board():
    # Set up the display
    board = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Hangmans game')

    # Defining colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    font = pygame.font.SysFont('Constantia', 20)

    #define global variable
    clicked = False
    class button():

        #colours for button and text
        button_col = (255, 0, 0)
        hover_col = (75, 225, 255)
        click_col = (50, 150, 255)
        text_col = BLACK
        width = 180
        height = 70

        def __init__(self, x, y, text):
            self.x = x
            self.y = y
            self.text = text

        def draw_button(self):

            global clicked
            action = False

            #get mouse position
            pos = pygame.mouse.get_pos()

            #create pygame Rect object for the button
            button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
            
            #check mouseover and clicked conditions
            if button_rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]== 1:
                    clicked = True
                    pygame.draw.rect(board, self.click_col, button_rect)
                elif pygame.mouse.get_pressed()[0]== 0 and clicked == True:
                    clicked = False
                    action = True
                else:
                    pygame.draw.rect(board, self.hover_col, button_rect)
            else:
                pygame.draw.rect(board, self.button_col, button_rect)

            #add text to button
            text_img = font.render(self.text, True, self.text_col)
            text_len = text_img.get_width()
            board.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
            return action

    again = button(70, 250, 'Play Again?')
    quit = button(550, 250, 'Quit?')
    global pressed 
    pressed = False
    # for the alphabets
    class but_1():
            
        #colours for button and text
        button_col = (0, 0, 0)
        hover_col = (128, 128, 128)
        click_col = (229, 228, 226)
        text_col = WHITE
        width = 50
        height = 50

        def __init__(self, x, y, text):
            self.x = x
            self.y = y
            self.text = text

        def draw_button_1(self):
            global pressed
            action = False

            # gets mouse position
            pos = pygame.mouse.get_pos()

            #create pygame Rect object for the button
            button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
            
            #check mouseover and clicked conditions
            if button_rect.collidepoint(pos):
                if pygame.mouse.get_pressed() == 1:
                    pressed = True
                    pygame.draw.rect(board, self.click_col, button_rect)
                elif pygame.mouse.get_pressed() == 0 and clicked == True:
                    pressed = False
                    action = True
                else:
                    pygame.draw.rect(board, self.hover_col, button_rect)
            else:
                pygame.draw.rect(board, self.button_col, button_rect)
            
            
            #add text to button
            text_img = font.render(self.text, True, self.text_col)
            text_len = text_img.get_width()
            board.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
            return action

    # will do this using a loop!!
    a = but_1(70,400, 'A')
    b = but_1(150,400, 'B')
    c = but_1(230,400, 'C')
    d = but_1(310,400, 'D')
    e = but_1(390,400, 'E')
    f = but_1(470,400, 'F')
    g = but_1(550,400, 'G')
    h = but_1(630,400, 'H')
    
    # Main loop of 2nd screen
    
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

            if again.draw_button():
                print('Again')
            if quit.draw_button():
                print('Quit')
                running = False
            # will do this using a loop!!    
            if a.draw_button_1():
                print('A')
            if b.draw_button_1():
                print('B')
            if c.draw_button_1():
                print('C')
            if d.draw_button_1():
                print('D')
            if e.draw_button_1():
                print('E')
            if f.draw_button_1():
                print('F')
            if g.draw_button_1():
                print('G')
            if h.draw_button_1():
                print('H')

            # Update the display
            pygame.display.update()

        

initial_board()

