print("Welcome to the tip calculator!")
# Option 1 - put value into variables
Bill = float(input("What was the total bill? $"))
Tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
Split = int(input("How many people to split the bill? "))

# convert Tip to a % value
Percentage = 1+Tip/100

# Round off Total value in 2 decimal places
TotalValue = round((Bill / Split) * Percentage,2)
print("Each person should pay: ${0}".format(TotalValue))
# Removed Thank you message, this is for debugging purposes only
# print("Thank you!")