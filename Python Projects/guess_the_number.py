#DAY 4
#Project_12
#Number Guessing Game

from random import randint
logo= """
  ___                       _   _                __                 _                
  / _ \_   _  ___  ___ ___  | |_| |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __  
 / /_\/ | | |/ _ \/ __/ __| | __| '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__| 
/ /_\\| |_| |  __/\__ \__ \ | |_| | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |_   
\____/ \__,_|\___||___/___/  \__|_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_(_)  
                                                                                      
"""
print(logo)
print("Welcome to Number guessing Game.")
print("I am thinking about a number between 1 and 100.")
guess= randint(1,100)
game_state= True
def guess_checker(num):
    if num>guess:
        print("Too High.")
        print("Guess Again.")
    elif num<guess:
        print("Too Low.")
        print("Guess Again.")
    elif num>100 or num<1:
        print("Wrong Input")
        print("Guess again")
difficulty= input("Choose Difficulty! Type 'easy' or 'hard': ").lower()
if difficulty=='easy':
    game_duration= 10
    while game_duration>0:
        print(f"You have {game_duration} attempts remaining to guess the number.")
        user_guess= int(input("Make a guess: "))
        if game_duration==1:
            pass
        else:
            guess_checker(user_guess)
        if user_guess==guess:
            print("You Won.")
            game_state= False
            break
        game_duration-=1

elif difficulty=='hard':
    game_duration= 5
    while game_duration>0:
        print(f"You have {game_duration} attempts remaining to guess the number.")
        user_guess= int(input("Make a guess: "))
        if game_duration==1:
            pass
        else:
            guess_checker(user_guess)
        if user_guess==guess:
            print("You Won.")
            game_state= False
            break
        game_duration-=1
if game_state== True:
    print("Pssst. You lost!. Number was ",guess)
