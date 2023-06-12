#DAY 4
#Project_11
#BlackJack card game[user advantage]

import art_project11, os
from random import randint
game_start_choice= input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
if game_start_choice=="y":
    game_state= True
    while game_state== True:
        os.system('cls')
        print(art_project11.logo)
        player_cards=[]
        pc_cards=[]
        for j in range(0,2):
            player_cards.append(randint(1,10))
            pc_cards.append(randint(1,10))
        while sum(player_cards)<=21:
            print("Your cards: ",player_cards)
            print("Computer's first card: ",pc_cards[0])
            re_choice= input("Type 'y' to get another card or 'n' to pass: ").lower()
            if re_choice=='y':
                temp_choice= int(input("Which card you wants to change? 1 or 2: "))
                if temp_choice==1:
                    player_cards[0]=randint(1,10)
                elif temp_choice== 2:
                    player_cards[1]= randint(1,10)
                else:
                    print("Wrong input!!")
                    continue
            else:
                print("Your final hand: ",player_cards)
                print("Computer's final hand:  ",pc_cards)
                break
        if sum(player_cards)==21:
            print("You Won!!")
            game_state= False
        elif sum(player_cards)>21:
            print("Computer Won!!")
            print("You lost.")
            game_state= False
        elif sum(player_cards)>sum(pc_cards):
            print("You Won!!")
            game_state= False
        else:
            print("Computer Won!!")
            print("You lost.")
            game_state= False
