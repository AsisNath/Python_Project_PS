import random


def roll_dice():
    roll = random.randint(1, 6)
    return roll


player1 = input("Enter player 1's name:\n")
player2 = input("Enter player 2's name:\n")
result1 = roll_dice()
result2 = roll_dice()

if result1 > result2:
    print(player1, " Wins & roll at ", result1,
          " & ", player2, "roll at ", result2)
elif result1 == result2:
    print(player1, " & ", player2, " have same value")
else:
    print(player2, " Wins & roll at ", result2,
          " & ", player1, "roll at ", result1)
