import random
import string


def main():
    # Get user input
    letter_count = int(input("How many letters would you like in your password?\n"))
    symbol_count = int(input("How many symbols would you like?\n"))
    number_count = int(input("How many numbers would you like?\n"))

    # Use String library to get all letter and digits. Only valid symbols are listed
    letter_list = [random.choice(string.ascii_letters) for i in range(letter_count)]
    number_list = [random.choice(string.digits) for i in range(number_count)]
    symbol_list = [random.choice(['!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']']) for i in range(symbol_count)]

    # Combine all list then shuffle
    combined_list = letter_list + symbol_list + number_list
    random.shuffle(combined_list)

    # Convert list to string with no spaces
    generated_pwd = "".join(str(element) for element in combined_list)
    print(f"Here is your password: {generated_pwd}")

    return 0


if __name__ == "__main__":
    main()