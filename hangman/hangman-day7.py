import random
from hangman_art import logo, stages
from os import system, name
from time import sleep
import re

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def wrong_guess(counter):
    counter -= 1
    print(stages[counter])

    return counter

def display_logo():
    print(logo)

def mask_char(word_str, rep_chr, pct):
    x = random.sample(rep_chr, round(pct))
    for ch in range(0, len(x)):
        # Replace char to _
        word_str = word_str.replace(x[ch], "_")
    return word_str, x

def set_difficulty(word_str, pct):
    # easy (0) = 25 %, medium (1) = 50 %, hard (2) = 75 %, geek (3) = 100 %
    if pct == 0:
        diff_percentage = 0.25
    elif pct == 1:
        diff_percentage = 0.50
    elif pct == 2:
        diff_percentage = 0.75
    else:
        diff_percentage = 1
    guess_diff = len(word_str) * diff_percentage

    return guess_diff

def init():
    game_ends = False
    life_ctr = len(stages)-1


    # Display welcome message
    display_logo()

    sleep(3)
    clear()

    # Choose difficulty easy = 25%, medium = 50%, hard = 75%, geek = 100%
    # choice_diff = input("Choose your difficulty. Type 0 = Easy, 1 = Medium, 2 = Hard, 3 = Geek Mode!\n")

    while True:
        try:
            # Open text file to retrieve a random word
            word = open("word_list.txt", "r").read().split()
            chosen_word = random.choice(word).upper()

            choice_diff = int(input("Choose your difficulty. Type 0 = Easy, 1 = Medium, 2 = Hard, 3 = Geek Mode, "
                                    "4 to exit game!\n"))
            if len(str(choice_diff)) > 1:
                print("Input is more than the allowed digit. Type 0 = Easy, 1 = Medium, 2 = Hard, 3 = Geek Mode, "
                      "4 to exit game!")
            elif choice_diff == 4:
                print("Too bad! Exiting the game...\n")
                break
            else:
                clear()
                # chosen_word = "TESTINGONLY"
                # print(f"**** FOR DEBUGGING ONLY: Your word is = {chosen_word} ****")

                # Get index and char value in chosen_word, make sure it is not space or a number
                replace_char_in_word = [i for i, i in enumerate(chosen_word) if not chosen_word.isspace() or chosen_word.isdigit()]

                # Determine difficulty by setting percentage of how many blanks will be displayed in the chosen_word
                pct_diff = set_difficulty(chosen_word, choice_diff)

                # Get random characters to be replaced in the chosen_word based on the difficulty set
                masked_char, char_ans = mask_char(chosen_word, replace_char_in_word, pct_diff)

                print(f"Guess the word: {masked_char}")

                while game_ends != True:
                    try:
                        guess = input(f"What is the letter of your guess for the {len(chosen_word)} letter word:\n").upper()
                        if guess not in chosen_word:
                            life_ctr = wrong_guess(life_ctr)
                            print(f"Remaining life = {life_ctr}")
                            if life_ctr == 0:
                                game_ends = True
                                print("GAME OVER! Try again!\n")
                        else:
                            indexes = []
                            # Handle duplicate character in the chosen_word
                            # If guess is correct and is showing more than 1 in the word, do this
                            for i, v in enumerate(chosen_word):
                                if chosen_word.count(v) > 1 and chosen_word[i] == guess:
                                    indexes.append(i)

                            masked_char = list(masked_char)

                            if guess in masked_char:
                                print("Letter already exist! Please guess another letter")
                            else:
                                for ch in range(0,len(masked_char)):
                                    for i in range(0,len(indexes)):
                                        if ch == indexes[i]:
                                            masked_char[ch] = guess

                                # Non duplicate character
                                for x, b in enumerate(chosen_word):
                                    if chosen_word.count(b) == 1 and chosen_word[x] == guess:
                                        masked_char[x] = guess
                                masked_char = ''.join(masked_char)

                                if masked_char.find('_') == -1:
                                    print(f"\nGood job! You guessed the word \"{chosen_word}\"\n")
                                    print("Try again!\n")
                                    sleep(2)
                                    clear()
                                    break
                                else:
                                    print("You're correct, but not done yet!\n")
                                print(masked_char)
                    except:
                        pass
        except ValueError:
            print("Input is not a number. Type 0 = Easy, 1 = Medium, 2 = Hard, 3 = Geek Mode!")



    return 0

if __name__ == "__main__":
    init()