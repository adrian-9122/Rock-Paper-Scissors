# Rock Paper Scissors

import random

def rps():
    playerWins = 0
    opponentWins = 0
    restart = True
    while restart == True:
        print("Player wins: ", playerWins)
        print("Opponent Wins: ", opponentWins)
        choice = input("Please enter 1 for Rock, 2 for Paper, or 3 for Scissors or 4 to exit")
        possibleChoices = ["1", "2", "3", "4"]
        opponentChoice = possibleChoices[random.randint(0,3)]
        while choice not in possibleChoices:
            print("Error, please enter a valid choice")
            choice = input("Please enter 1 for Rock, 2 for Paper, or 3 for Scissors or 4 to exit")
        if choice == "4":
            break
            
        if choice == opponentChoice:
            print("Tie!")
        elif choice == "1" and opponentChoice == "2":
            opponentWins += 1
            print("You lose, paper beats rock!")
        elif choice == "1" and opponentChoice == "3":
            playerWins += 1
            print("You win, rock beats scissors!")
        elif choice == "2" and opponentChoice == "1":
            playerWins += 1
            print("You win, paper beats rock!")
        elif choice == "2" and opponentChoice == "3":
            opponentWins += 1
            print("You lose, scissors beats paper!")
        elif choice == "3" and opponentChoice == "1":
            opponentWins += 1
            print("You lose, rock beats scissors!")
        else:
            playerWins += 1
            print("You win, scissors beats paper!")
        
rps()
