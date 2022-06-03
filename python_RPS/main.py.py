#Rules of the game 
#Rock smashes Scissors
#Paper covers Rock 
#Scissors cuts Paper
from multiprocessing import RLock
import random
# from secrets import choice

game_on = True

while game_on:
    print("Please pick an option from the list")

    possible_actions = ["R", "P", "S"]

    user_action = input("Enter a choice (R, P, S): ")  
    # R = Rock
    # P = Paper
    # S = Scissors
    try:
        possible_actions = ["R", "P", "S"]
    except ValueError as e:
        print(f"Invalid selection. Enter a value in range {user_action}")
        continue


    computer_action = random.choice(possible_actions)
    print(f"\n Player ({user_action}) : CPU ({computer_action}).\n")

    if user_action == computer_action:
        print("It's a tie, Please try again")
    elif user_action == "R":
        if computer_action == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! Oops! You lose.")
    elif user_action == "P":
        if computer_action == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! Oops! You lose.")
    elif user_action == "S":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! Oops! You lose.")
    else:
        print("Invalid Option, input a valid option")
    
    choice = input("Will you want to play again? [y,n]")

    if choice == "y":
        pass

    if choice == "n":
        game_on = False
        print("GAME OVER THANK YOU FOR PLAYING")

    