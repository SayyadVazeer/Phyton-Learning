import random

low = 1
high = 100
answer = random.randint(low,high)
is_running = True
guesses = 0
print("Phyton Number Guessing Game ")
print(f"You have to guess an number between {low} snd {high} :")

while is_running:
    guess = input("Enter Your guess : ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < low or guess > high:
            print(f"Number out of Range \nChoose num between {low} and {high}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too High! Try again!")
        else:
            print("------* Congratulations *------")
            print(f"Your Guess {answer} is Correct ")
            print(f"You gussed it in {guesses} no of guesses")