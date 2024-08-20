from random import *
from datetime import *
import os
def name():
    print("                               NUMBER GUESSING GAME")
j=1
score=0
while (j==1):
    #number guessing game
    os.system('cls')
    print("                        hint:the number is between 0 and 6.")
    b=randrange(0,6)
    for i in range(3):
        name()
        print("                        you have",(3-i),"try left.")
        a=input("                        enter the number you have guessed:")
        c=int(a)   
        if (c==b):
            os.system('cls')
            print("                            you won at",end=" ")
            score=score+1
            break
        else:
            print("try again")
            os.system('cls')
            if(i==2):
                print("tne number was",b)
                print("               you lose at",end=" ")
    print(datetime.now())
    print()
    print("Do you want to play again.")
    a=input("if yes enter YES if no enter NO:")
    b=a.upper()
    if(b=="YES"):
        j=1
    elif(b=="NO"):
        j=0 
    else:
        print("you enter invalid word:")
        j=0
os.system('cls')
print()
print()
print("                              YOUR SCORE IS",score)
print()
print("_______________________________________________GAME ENDS_______________________________________________________")   
print() 
print()   


    



