#
# Author: yilmazturkm
# Author Github: https://github.com/yilmazturkm
# Author Url: https://yilmazturk.gen.tr
# 
# Guessing game with python.
# It select a random number and wants user to guess the number. If number is lower then user's input,
# it helps user by saying the number is lower. If number is higher then user's input, it says the number is greater.
#


# import random module
import random

# while loop to play until user exits
while True:
    num = random.randint(1,100) # select a random number between 1-100
    counter = 1 # counter for guess
    while True:
        guess = input("Guess the number (q for exit): ") # get user's input
        # if else statement to compare the user input
        if guess.lower() == "q": # if user input is q
            print(f"Exiting from the game... The number was {num}")
            break # exit the game
        else:
            try:
                guess = int(guess) # convert user input to int
                # if else statement to compare the user's guess with number
                if guess == num: # if user find the number
                    # print win message with guess counter
                    print(f"You found the number {num}\nYou took {counter} guesses to find the number {num}")
                    break # exit the game
                elif guess > num: # if user's guess is greater than number
                    # print an info message
                    print(f"The number you are looking for is lower than {guess}")
                elif guess < num: # if user's guess is lower than number
                    # print an info message
                    print(f"The number you are looking for is greater than {guess}")
            except Exception as e: # catch the faults
                print(f"Error: {e}")
        counter += 1 # increase counter for every guess
    # ask user if he/she wants more game
    question = input("Would you like to play one more time? (y/n): ") # get user input
    # if else statement to compare user input
    if question.lower() == "y":
        continue # start over
    elif question.lower() == "n":
        print("See you!")
        break # exit game
    else:
        print("Wrong choice... Exiting from app...")
        break # exit game
    
    
