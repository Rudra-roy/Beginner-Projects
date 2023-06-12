#DAY 1
#Project_3
#Tresure_find(Easy)
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
print("Welcome to Tresure Island.")
print("Your mission is to find the tresure.")
print("=========================================================")
temp=input("(Press Enter to Countinue)")
print("Going forward a fork appeard!!!",end="")
choice1=input("Which path will you choose?(Left or Right)").lower()
if choice1=="left":
    print("Going into Left path have lead you to Beautifull Lake. There is a sign saying 'Wait here or swim across the lake!' choice is yours! ")
    choice2=input("What will you do?(Swim or Wait)").lower()
    if choice2=="wait":
        print("after waiting some time suddenly 3 doors appeared and a sign saying 'Go through One door and you shall find your DESTINY!!'")
        choice3=input("Which door will you choose?(Red, Yellow, Blue)").lower()
        if choice3=="yellow":
            print("CONGRATULATIONS my child!!")
            print("You've found your destiny!!")
            print("All the tresure is your's")
        else:
            print("You've reached your DESTINY!!!! DEATH!!!!")
            print("GAME OVER!!!")
    else:
        print("There are lake monsters in the lake. You Died!!")
        print("GAME OVER!!!")
else:
    print("Wrong Path!!!!")
    print("GAME OVER!!!")