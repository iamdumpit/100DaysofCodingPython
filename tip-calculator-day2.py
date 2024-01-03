print("Welcome to the tip calculator!")
# Option 1 - put value into variables
Bill = float(input("What was the total bill? $"))
Tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
Split = int(input("How many people to split the bill? "))
Percentage = 1+Tip/100

TotalValue = round((Bill / Split) * Percentage,2)
print("Each person should pay: ${0}".format(TotalValue))