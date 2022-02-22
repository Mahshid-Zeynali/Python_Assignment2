import random

while True : 
    dice = random.randint(1,6)
    print("Number of dice: ",dice)
    if(dice != 6) :
        break
    elif(dice == 6) :
        print("You can roll the dice again")
