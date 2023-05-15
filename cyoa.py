print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

option1 = input("You find yourself at a crossroad. You can go left or right. Which way do you choose? (Choose left or right)\n").lower()
option2 = input("You decide to take the left path and find yourself at a lake. You wonder if you should swim or if you should wait for help. Which do you choose? (Choose swim or wait)\n").lower()
option3 = input("As you wait, you find three doors not far off. One is red, one is yellow, and the other is blue. Which will you go through? (Choose red, yellow, or blue)\n").lower()

if option1 == "left":
  if option2 == "wait":
    if option3 == "yellow":
      print("It's highly unlikely you managed to get this far on your first try, but regardless, you won! You get the treasure and buy property in the Bay Area before the housing market explodes, making you rich enough to create a movie which will be considered a cult classic by some while considered the worst movie of all time by others.")
    elif option3 == "blue":
      print("You wondered past the blue door and were immediately eaten by bats. Game over.")
    elif option3 == "red":
      print("You stepped through the red door and were immediately set on fire. Game over.")
    else:
      print("Idk, man. You just died. Game over.")
  else:
    print("You were attacked by trout and died. Game over.")
else:
  print("You fell into a hole and died. Game over.")
