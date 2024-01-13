from logo import print_logo
from os import system, name
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def caesar_cipher(direction, raw_msg, shift):
    ciphered_text = []
    if direction.lower() == 'decode':
        shift *= -1

    for ch in raw_msg:
        if ch in alphabet:
            old_ch_index = alphabet.index(ch)
            new_ch_index = old_ch_index + shift
            if new_ch_index > 26:
                new_ch_index = new_ch_index % 26
            ciphered_text.append(alphabet[new_ch_index])
        else:
            ciphered_text.append(ch)

    return ''.join(ciphered_text)


try_again = True
print_logo()

while try_again:
    cipher_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input(f"Type your message to be {cipher_direction}d:\n")
    shift_num = int(input("Type the shift number:\n"))

    print(f"Here's the {cipher_direction}d result: {caesar_cipher(direction=cipher_direction, raw_msg=message, shift = shift_num)}")

    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if go_again.lower() == 'no':
        try_again = False
        print("Bye bye!...")
    else:
        clear()

