import random
import Wordslist
from Wordslist import words

hangman_art = {
    0:("   ",
       "   ",
       "   "),
    1:(" O ",
       "   ",
       "   "),
    2:(" O ",
       " | ",
       "   "),
    3:(" O ",
       "/| ",
       "   "),
    4:(" O ",
       "/|\\",
       "   "),
    5:(" O ",
       "/|\\",
       "/  "),
    6:(" O ",
       "/|\\",
       "/ \\")
}

def display_man(wrong_guess):
    print("****")
    for line in hangman_art[wrong_guess]:
        print(line)
    print("****")
def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ")
        print()
        if len(guess) != 1 or not guess.isalpha() :
            print("Invalid iput! ")
            continue
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue
        
        guessed_letters.add(guess)
        
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1


        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print ("You WIN !")
            is_running = False
        elif wrong_guesses >= len(hangman_art)-1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You LOSE!")
            is_running = False


if __name__ =='__main__':
    main()