from logo import print_logo
from os import system, name

class Calculator:

    def __init__(self, initial_num: float, next_num: float, operator_val: str):
        self.initial_num = initial_num
        self.next_num = next_num
        self.operator_val = operator_val
        self.total_num = self.initial_num

    def clear_screen(self):
        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def add_numbers(self):
        return self.initial_num + self.next_num

    def subtract_numbers(self):
        return self.initial_num - self.next_num

    def multiply_numbers(self):
        return self.initial_num * self.next_num

    def divide_numbers(self):
        return self.initial_num / self.next_num

    def calculate_number(self):
        if self.operator_val == "+":
            self.total_num = self.add_numbers()
        elif self.operator_val == "-":
            self.total_num = self.subtract_numbers()
        elif self.operator_val == "*":
            self.total_num = self.multiply_numbers()
        elif self.operator_val == "/":
            self.total_num = self.divide_numbers()
        else:
            return print("\nInvalid Symbol or Operator. Cannot calculate number")
        return print(f"{self.initial_num} {self.operator_val} {self.next_num} = {self.total_num}")

def init():

    operations = {
        "+": "add",
        "-": "subtract",
        "*": "multiply",
        "/": "divide",
    }

    print_logo()
    num1 = float(input("What's the first number?: "))

    continue_calc = True

    while continue_calc:
        for symbols in operations:
            print(symbols)
        operator_value = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculator = Calculator(num1, num2, operator_value)
        calculator.calculate_number()

        if input(f"Type 'y' to continue calculating with {calculator.total_num}, or type 'n' to start a new calculation: ").lower() == 'y':
            num1 = calculator.total_num
        else:
            continue_calc = False
            calculator.clear_screen()
            init()

    return 0

if __name__ == "__main__":
    init()