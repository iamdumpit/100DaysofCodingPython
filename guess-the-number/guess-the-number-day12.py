from logo import print_logo
from os import system, name
from time import sleep
from colorama import Fore, Back, Style
import random

EASY_TURNS = 10
HARD_TURNS = 5


class GuessTheNumber:

    def __init__(self):
        self.number_guess = random.randint(1, 100)
        self.difficulty = ""
        self.tries = 0
        self.answer_flag = 0
        pass

    def set_difficulty(self, setup: str):
        if self.difficulty == 'easy':
            self.tries = EASY_TURNS
        else:
            self.tries = HARD_TURNS

        return self.tries

    def check_answer(self, guess: int):
        if guess == self.number_guess:
            self.answer_flag = self.number_guess
            return print(f"{Fore.LIGHTGREEN_EX}You got it! The answer was {self.number_guess} {Style.RESET_ALL}")
        elif guess < self.number_guess:
            self.answer_flag = 0
            self.tries -= 1
            return print(f"{Fore.LIGHTRED_EX}Too low.\nGuess again.\nYou have {self.tries} {Style.RESET_ALL}")
        else:
            self.answer_flag = 0
            self.tries -= 1
            return print(f"{Fore.LIGHTRED_EX}Too high.\nGuess again.\nYou have {self.tries} {Style.RESET_ALL}")

    @staticmethod
    # Made it static as this has relationship w/ the class but not unique per instance
    def clear_screen():
        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')


def init():
    print_logo()

    guess_the_number = GuessTheNumber()
    # Debugging purposes only, show answer
    # print(guess_the_number.number_guess)

    guess_the_number.difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()

    sleep(1)
    GuessTheNumber.clear_screen()

    print(f"You have {guess_the_number.set_difficulty(guess_the_number.difficulty)} attempts remaining to guess the "
          f"number")

    while guess_the_number.answer_flag != guess_the_number.number_guess:
        answer = input("Make a guess:\n")
        guess_the_number.check_answer(int(answer))
        sleep(1)
    return 0


if __name__ == "__main__":
    init()
