import random

print("Welcome to Rock Paper Scissors Game!")

preChoice = ["Rock", "Paper", "Scissor"]

computerChoice = random.randint(0, 2)

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor: "))

if 0 <= userChoice <= 2:
    print(f"Your choice is: {preChoice[userChoice]}")
    print(f"Computer choice is : {preChoice[computerChoice]}")


if userChoice < 0 or userChoice >= 3 :
    print("You entered an invalid number, YOU LOSE")
elif userChoice == 0 and computerChoice == 2:
    print("You WIN")
elif computerChoice == 0 and userChoice == 2:
    print("You Lose")
elif computerChoice > userChoice:
    print("You LOSE")
elif userChoice > computerChoice:
    print("You WIN!")
elif userChoice == computerChoice:
    print("It's a DRAW")


