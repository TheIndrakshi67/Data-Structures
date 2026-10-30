import math
import random
dice_options=[1,2,3,4,5,6]
print("Let's play a game")
points=0

def play_turn(user_choice):
    global points
    if user_choice=='1':
        print("You have selected Taj hotel to visit")
        points +=1
    elif user_choice=='2':
        print("You have selected Agra palace to visit")
        points +=2
    elif user_choice=='3':
        print("You have selected Dubai")
        points+=3
    elif user_choice=='4':
        print("You have selected Singapore to visit")
        points+=4
    elif user_choice=='5':
        print("You have selected Bhopal to visit")
        points+=5
    else:
        print("You selected to Juhu to visit")
user_input=input("Enter your choice (1-6)")
play_turn(user_input)

player1=input("Press enter to throw a dice")
if player1 == '':
    print("Player 1 rolled:", random.choice(dice_options))
player2=input("Press enter to throw dice")
if player2=='':
    print("Player 2 rolled: ", random.choice(dice_options))