from logo import print_logo
from os import system, name
from time import sleep
from colorama import Fore, Back, Style
import random


class BlackJack:

    def __init__(self):
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.user_cards = []
        self.computer_cards = []

    def deal_cards(self):
        random_card = random.choice(self.cards)
        self.cards.remove(random_card)
        return random_card

    def shuffle_deck(self):
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    @staticmethod
    # Made it static as this has relationship w/ the class but not unique per instance
    def compute_score(current_cards: list):

        if sum(current_cards) == 21 and len(current_cards) == 2:
            # Returns 0 for the winner
            return 0

        # TODO #2 Detect when computer or user has a blackjack. (Ace + 10 value card).
        # TODO #5 If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
        # Checker for Ace. Converts value to 1 if score is greater than 21
        # Otherwise, retain to 11
        if 11 in current_cards and sum(current_cards) > 21:
            current_cards.remove(11)
            current_cards.append(1)

        return sum(current_cards)


    def determine_winner(self, player_score: int, computer_score: int):

        # TODO #3 If computer gets blackjack, then the user loses (even if the user also has a blackjack).
        #  If the user gets a blackjack, then they win (unless the computer also has a blackjack).
        # TODO #10 Compare user and computer scores and see if it's a win, loss, or draw.
        if player_score == computer_score:
            return "Draw 🙃"
        elif computer_score == 0:
            return "Lose, opponent has Blackjack 😱"
        elif player_score == 0:
            return "Win with a Blackjack 😎"
        elif player_score > 21:
            return "You went over. You lose 😭"
        elif computer_score > 21:
            return "Opponent went over. You win 😁"
        elif player_score > computer_score:
            return "You win 😃"
        else:
            return "You lose 😤"

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
    sleep(1)
    BlackJack.clear_screen()
    blackjack = BlackJack()
    game_over = False

    # TODO #1 Deal both user and computer a starting hand of 2 random card values.
    for initial_cards in range(2):
        blackjack.user_cards.append(blackjack.deal_cards())
        blackjack.computer_cards.append(blackjack.deal_cards())

    while not game_over:
        sleep(0.5)
        BlackJack.clear_screen()

        # TODO #4 Calculate the user's and computer's scores based on their card values.
        user_score = BlackJack.compute_score(blackjack.user_cards)
        comp_score = BlackJack.compute_score(blackjack.computer_cards)

        print(f"Your cards: {blackjack.user_cards}, "
              f"Current Score: {user_score}")

        # TODO #6 Reveal computer's first card to the user.
        print(f"Computer's first card: {blackjack.computer_cards[0]}")

        # TODO #9 Once the user is done and no longer wants to draw any more cards, let the computer play.
        #  The computer should keep drawing cards unless their score goes over 16.
        while comp_score < 17 and comp_score != 0:
            blackjack.computer_cards.append(blackjack.deal_cards())
            comp_score = BlackJack.compute_score(blackjack.computer_cards)

        # Shuffle deck after all cards are drawn
        if len(blackjack.cards) == 0:
            print("Reshuffling Deck...")
            blackjack.shuffle_deck()

        # TODO #7 Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack.
        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            # TODO #8 Ask the user if they want to get another card.
            if input(f"Type 'y' to get another card (HIT) , type 'n' to pass (STAND): ").lower() == 'y':
                sleep(0.5)
                BlackJack.clear_screen()
                blackjack.user_cards.append(blackjack.deal_cards())
                user_score = BlackJack.compute_score(blackjack.user_cards)
                print(f"Your cards: {blackjack.user_cards}, "
                      f"Current Score: {user_score}")
                print(f"Computer's first card: {blackjack.computer_cards[0]}")
            else:
                game_over = True

    sleep(1)
    BlackJack.clear_screen()

    # TODO #11 Print out the player's and computer's final hand and their scores at the end of the game.
    user_score = BlackJack.compute_score(blackjack.user_cards)
    comp_score = BlackJack.compute_score(blackjack.computer_cards)
    print(f"Your final hand: {blackjack.user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {blackjack.computer_cards}, final score: {comp_score}")
    print(f"{Fore.LIGHTGREEN_EX} {blackjack.determine_winner(user_score, comp_score)} \n {Style.RESET_ALL}")

    # TODO #12 After the game ends, ask the user if they'd like to play again.
    #  Clear the console for a fresh start.
    if input(f"Do you want to play again? Type 'y' or 'n': ").lower() != 'y':
        game_over = True
    else:
        BlackJack.clear_screen()
        init()

    return 0


if __name__ == "__main__":
    init()










