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
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a crossroad, where do you want to go? Type \"left\" or \"right\"")
response = input("Left or right? ").lower()
if response == "left":
    print("You are now in a river. You can \"swim\" or \"wait\"")
    response = input("Swim or wait? ").lower()
    if response == "wait":
        print("There are three doors, a \"red\" one, a \"yellow\" one, and a \"blue\" one.")
        response = input("Red, yellow, or blue? ").lower()
        if response == "blue":
            print("Eaten by beasts.\nGame Over.")
        elif response == "red":
            print("Burned by fire.\nGame Over.")
        elif response == "yellow":
            print("Found the treasure! You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")