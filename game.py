
# Library
import random
import pygame
import time
from initial_board import initial_board
from word_bank import easy_words, hard_words, idioms_list
import speech_recognition as sr


r = sr.Recognizer()
update_display = 0
################################################################################################


def player_version():
    choice = input("What version do you wanna play? Easy or hard.\n We also have the version 'idiom' or 'reversed version'")


def guessing(word, guess, blank_word):
    global update_display
    correct_guess = False
    for i in word:
        if len(guess) != 1:
            if guess == word:
                blank_word = word
                return True
        else:
            if guess.upper() == word[i]: 
                blank_word[i] = word[i]
                correct_guess = True

    if correct_guess == False:
        print(f"There is no {guess.upper()}!! Please try again :)")
        update_display += 1
        tries -= 1


def play_game(word):
    word_completion = "_" * len(word)
    guess = False
    tries = 6 
    print("I bet you can't win this game! Let's play Hangman")
    # print(display_board(tries))
    print(word_completion)
    while not guess and tries > 0:
        pass

