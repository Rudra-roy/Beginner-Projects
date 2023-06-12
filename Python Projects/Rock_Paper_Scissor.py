#DAY 2
#Project_4
#rock-paper-scissors game

from random import randint
print("##############################################################")
print("                 WELCOME TO ROCK-PAPER-SCISSORS")
print("##############################################################")

def player_icon(num):
    print("You Chose: ")
    print(opt[num])
def pc_icon(num):
    print("Computer Chose: ")
    print(opt[num])

rock=  '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper= '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors= """
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
opt=[rock, paper, scissors]

while True:
        
    player_choice=int(input("State your Choice: (0 for Rock),(1 for Paper),(2 for Scissors)"))
    pc_choice= randint(0,2)
    if player_choice in [0,1,2]:
        if player_choice==pc_choice:
            player_icon(player_choice)
            pc_icon(pc_choice)
            print("Ahhh, Its a Draw!")
            game_state=input("Want to play again?? (Yes or No)").lower()
            if game_state=="yes":
                continue
            else:
                break
        elif player_choice== 0 and pc_choice== 2:
            player_icon(player_choice)
            pc_icon(pc_choice)
            print("Hurrray!! You Won!!")
            game_state=input("Want to play again?? (Yes or No)").lower()
            if game_state=="yes":
                continue
            else:
                break
        elif pc_choice== 0 and player_choice== 2:
            player_icon(player_choice)
            pc_icon(pc_choice)
            print("Opps, Sorry You lost!!")
            game_state=input("Want to play again?? (Yes or No)").lower()
            if game_state=="yes":
                continue
            else:
                break
        elif pc_choice > player_choice:
            player_icon(player_choice)
            pc_icon(pc_choice)
            print("Opps, Sorry You lost!!")
            game_state=input("Want to play again?? (Yes or No)").lower()
            if game_state=="yes":
                continue
            else:
                break
        elif player_choice > pc_choice:
            player_icon(player_choice)
            pc_icon(pc_choice)
            print("Hurrray!!! You won!!!")
            game_state=input("Want to play again?? (Yes or No)").lower()
            if game_state=="yes":
                continue
            else:
                break
    else:
        print("Wrong choice!! Choice again!")