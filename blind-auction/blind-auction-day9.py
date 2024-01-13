from logo import print_logo
from os import system, name
from time import sleep

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def highest_bidder(bid_dict):

    winners_name = max(bid_dict, key=bid_dict.get)
    winners_value = max(bid_dict.values())
    clear()
    return f"The winner is {winners_name} with a bid of ${int(winners_value)}"

def init():
    print_logo()

    sleep(1)
    clear()

    try_again = True
    bidders_dict= {}
    while try_again:


        bidder_name = str(input("What is your name?:\n"))
        bid_amount = float(input("What is your bid?:\n$"))

        bidders_dict.update({bidder_name : bid_amount})

        go_again = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if go_again.lower() == 'no':
            try_again = False
            print(highest_bidder(bidders_dict))
        else:
            clear()

    return 0

if __name__ == "__main__":
    init()