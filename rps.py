import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")

playerchoice = input("Enter... \n1 for Rock,\n2 for Paper, \n3 for Scissors: \n\n")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter either: \n 1, 2, or 3.")

computerchoice = random.choice("123")

computer = int(computerchoice)

print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("Computer chose " + str(RPS(computer)).replace('RPS.', '') + ".")


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
3