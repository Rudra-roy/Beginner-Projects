#DAY 3
#Project_7
#HANGMAN game

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
def word_display():
    guessed_word=""
    for i in display_word:
        guessed_word+=i
    print(guessed_word)
    return guessed_word
from random_word import RandomWords
print(logo)
print()
print("Welcome to Hangman game!!!")
print("!!!Important notes!!!")
print("A man's life will be on the line. So play with caution!!")
temp=input("(Press Enter to Continue)")
word= RandomWords()
fw=word.get_random_word()
blank_len= len(fw)
display_word= []
for i in range(blank_len):
    display_word.append("_")

print("Your Word:   ","_"*blank_len)
lives=6
flag= False
while lives!=-1:

    player_choice=input("Your guess: ").lower()
    if word_display()==fw:
        word_display()
        print("You Won!!")
        flag= True
        break
    elif player_choice in fw:
        idx= fw.index(player_choice)
        display_word[idx]=player_choice
        word_display()
    else:
        print(f"You guessed {player_choice}. {player_choice} is not in the word. 1 life lost!!")
        print(stages[lives])
        lives-=1
        word_display()
if flag== False:
    print("Your Word was: ",fw)
    print("You lost!!")