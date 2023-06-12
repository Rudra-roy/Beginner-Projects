#DAY 3
#Projec_8
#Caesar cipher encoder-decoder

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

def encoder(string,num):
    encode=""
    for i in string:
        encode+=chr(ord(i)+num)
    return encode


def decoder(string,num):
    decode=""
    for i in string:
        decode+=chr(ord(i)-num)
    return decode

state= "on"

while state=="on":
    print("Type 'encode' to encrypt a message Or Type 'decode' to decrypt a message!")
    choice=input().lower()
    print("Type your message!")
    meassage=input()

    shift_choice=int(input("Type the shift number: "))
    if choice=="encode":
        encode=encoder(meassage,shift_choice)
        print("Here is the encoded result: ",encode)
        encode=""
        print("Type 'yes' if you want to go again, Otherwise type 'no'." ) 
        re_choice=input().lower()
        if re_choice=="yes":
            continue
        else:
            state="off"
    elif choice=="decode":
        decode=decoder(meassage,shift_choice)
        print("Here is the deocded result: ",decode)
        decode=""
        print("Type 'yes' if you want to go again, Otherwise type 'no'." ) 
        re_choice=input().lower()
        if re_choice=="yes":
            continue
        else:
            state="off"
    else:
        print("Wrong input!!")