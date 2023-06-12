#DAY 2
#Project_2
#Tip_calculator
print("Welcome to the tip calculator.")
print("$",end="")
bill=float(input())
print("What percentage tip would you like to give? 10, 12, or 15?")
tip=int(input())
print("How many people to split the bill?")
splitter=int(input())
print(f"Each person should pay: ${(bill+bill*(tip/100))/splitter}")