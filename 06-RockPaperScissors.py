#
# Author: yilmazturkm
# Author Github: https://github.com/yilmazturkm
# Author Url: https://yilmazturk.gen.tr
# 
# Rock Paper Scissors game with two players.
#

# while loop to play until player exits
while True:
    # Print the choices
    print("""
    Select a number
    1 - Rock
    2 - Scissors
    3 - Paper
    """)
    playerA = input("Player A's choice: ") # Get the 1st player's choice
    playerB = input("Player B's choice: ") # Get the 2nd player's choice

    # try-except to catch errors
    try:
        playerA = int(playerA) # convert char to int
        playerB = int(playerB) # convert char to int
        
        # if else statement to compare the players' choices
        if playerA == 1 and playerB == 2:
            print("Player A wins: Rock beats Scissors")
        elif playerA == 1 and playerB == 3:
            print("Player B wins: Paper beats Rock")
        elif playerA == 2 and playerB == 1:
            print("Player B wins: Rock beats Scissors")
        elif playerA == 2 and playerB == 3:
            print("Player A wins: Scissor beats Paper")
        elif playerA == 3 and playerB == 1:
            print("Player A wins: Paper beats Rock")
        elif playerA == 3 and playerB == 2:
            print("Player B wins: Scissor beats Paper")
        elif playerA == playerB:
            print("Drawn")
        else:
            print("Wrong choice: Type one of the numbers (1, 2, 3)")
        
        # Ask users if they want to play more games
        question = input("One more game? (y/n): ")
        
        # if else statement to check the user input
        if question.lower() == "y":
            print("Another game will be started...")
            continue
        elif question.lower() == "n":
            print("Quiting from game...")
            break
        else:
            print("Error: Wrong input. Quiting from game...")
            break
    
    # Throw an exception
    except Exception as e:
        print(f"Error: {e}")
