import random

computer_choice = random.choice(['rock', "paper", "scissors"])
user_choice = input("Enter your choice ( rock, paper, or scissors):\n")

if computer_choice == user_choice:
    print("Tie: " + "Computer choice is: " + computer_choice)
elif user_choice == "rock" and computer_choice == "scissors":
    print("Win: " + "Computer choice is: " + computer_choice)
elif user_choice == "paper" and computer_choice == "rock":
    print("Win: " + "Computer choice is: " + computer_choice)
elif user_choice == "scissors" and computer_choice == "Paper":
    print("Win: " + "Computer choice is: " + computer_choice)
else:
    print("You lose, Computer Wins:" + "Computer choice is: " + computer_choice)
