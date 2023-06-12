#DAY 2
#Project_5
#Password Generetor


from random import randint,choice,shuffle
print("***********************************************")
print("Welcome to Py-Password Generator!")
print("***********************************************")
print("How many letters would you like in your password?")
letter_count= int(input())
small_letter_count= randint(1,letter_count)
password=""
for i in range(small_letter_count):
    j= randint(97,122)
    password+=chr(j)
for i in range(letter_count-small_letter_count):
    j= randint(65,90)
    password+=chr(j)
print("How many symbols would you like?")
sym_count= int(input())
symbols=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
for i in range(sym_count):
    j= choice(symbols)
    password+=j
print("How many numbers would you like?")
num_count= int(input())
for i in range(num_count):
    j= randint(48,57)
    password+=chr(j)
password_list=[]
for i in password:
    password_list.append(i)
shuffle(password_list)
shuffled_password= ""
for i in password_list:
    shuffled_password+=i
print("Here is your Password: ",shuffled_password)