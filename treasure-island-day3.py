print('''

*******************************************************************************
                 _____
              .-" .-. "-.
            _/ '=(0.0)=' \_
          /`   .='|m|'=.   `\
          
          \________________ /
      .--.__///`'-,__~\\\\~`
     / /6|__\// a (__)-\\\\
     \ \/--`((   ._\   ,)))
     /  \\  ))\  -==-  (O)(
    /    )\((((\   .  /)))))
   /  _.' /  __(`~~~~`)__
  //"\\,-'-"`   `~~~~\\~~`"-.
 //  /`"              `      `\
//
******************************************************************************* 

''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

direction = str(input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n"))
if direction.lower() != 'left':
    print("Fall into a hole.\nGame Over")
else:
    action = str(input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n"))
    if action.lower() == 'wait':
        color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        if color.lower() == 'red':
            print("Burned by fire.\nGame Over")
        if color.lower() == 'blue':
            print("Eaten by beasts.\nGame Over")
        if color.lower() == 'yellow':
            print("You found the treasure! You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.\nGame Over")
