import sys
import random
from enum import Enum


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input(
        "\nEnter... \n1 for Rock,\n2 for Paper, \n3 for Scissors: \n\n"
    )
    if playerchoice not in ["1", "2", "3"]:
        print("You must enter either: \n 1, 2, or 3.")
        return play_rps()

    player = int(playerchoice)

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("You chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Computer chose " + str(RPS(computer)).replace("RPS.", "") + ".")

    # determining who the winner is using this control flow statement

    if computer == 2 and player == 1:
        print("😣 You lost")
    elif computer == 1 and player == 3:
        print("😣 You lost")
    elif computer == 3 and player == 2:
        print("😣 You lost")
    elif computer == player:
        print("The game was a draw. \n Play again")
    else:
        print("🎉 You Won")

    print("\n Play again? ")

    while True:
        playagain = input("\n Kindly Press: \n Y for yes or \n Q to quit \n\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n 🎉🎉🎉🎉🎉")
        print("Thank you for playing")
        sys.exit()


play_rps()
