from logo import print_logo, print_vs
from game_data import data
from os import system, name
from time import sleep
import random


class HigherLower:

    def __init__(self):
        self.primary = {}
        self.secondary = {}
        self.score = 0
        self.correct_answer = ""

    @staticmethod
    def get_random_account():
        x = random.choice(data)
        data.remove(x)
        return x

    @staticmethod
    def format_account(account):
        account_name = account["name"]
        description = account["description"]
        country = account["country"]

        return f"{account_name}, {description}, from {country}"

    @staticmethod
    def check_answer(ans: str, pri: dict, sec: dict):

        if pri["follower_count"] > sec["follower_count"]:
            return ans == "a", pri
        else:
            return ans == "b", sec

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
    # name, description = random.choice(list(data.ke()))

    is_over = False
    higher_lower = HigherLower()
    higher_lower.primary = higher_lower.get_random_account()
    higher_lower.secondary = higher_lower.get_random_account()

    while not is_over:
        sleep(1)
        higher_lower.clear_screen()
        print(f"Compare A: {higher_lower.format_account(higher_lower.primary)}")
        print_vs()
        print(f"Against B: {higher_lower.format_account(higher_lower.secondary)}")

        answer = input("\nWho has more followers? Type 'A' or 'B': ").lower()
        is_correct, correct_ans = higher_lower.check_answer(answer, higher_lower.primary, higher_lower.secondary)

        if is_correct:
            higher_lower.score += 1
            higher_lower.primary = correct_ans
            higher_lower.secondary = higher_lower.get_random_account()

            print(f"You're correct! Current score: {higher_lower.score}")
            sleep(1)
        else:
            print(f"Sorry. That's incorrect. Your final score is {higher_lower.score}")
            is_over = True


if __name__ == "__main__":
    init()
