import random

options = ("rock","paper","scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    player = input("Enter a choice (rock, paper, scissors): ")
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player  : {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a TIE!")
    elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
        print("------* Congrats You Won! *------")
    else:
        print("Sorry You Loose! Better luck next time ")
    
    if not input("Play again? (y/n): ").lower() == "y":
        running = False
print("Thank you for playing!")

