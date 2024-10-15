
# Library
import time
from word_bank import hangman_word
from time import sleep
from sys import stdout

def display_board():
    for i in range(0, 1000):
        stdout.write("\b")
        sleep(.9)
        stdout.write("\b\b\b>>>" + str(i))
        stdout.flush()

def correct_char(word, char):
    if char in word:
        return True
    
    return False

def list_characters():
    pass

def play_game():
    word = hangman_word(word)
    word_completion = "_ " * len(word)
    guess = False
    tries = 6 
    print("I bet you can't win this game! Let's play Hangman")
    print(display_board(tries))
    print(word_completion)
    while not guess and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and correct_char(word, guess):
            pass
        elif guess == word:
            pass
        else: 
            print("Not a correct one, try again!!")
            tries -= 1

