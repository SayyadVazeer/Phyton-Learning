questions = ("What is the capital city of Canada?",
             "Which element has the chemical symbol 'Fe'?",
             "In what year did the Titanic sink?",
             "Who painted the ceiling of the Sistine Chapel?",
             "Which planet is known as the 'Red Planet'?")
options = (("A.Toronto","B.Vancouver","C.Montreal","D.Ottawa"),
           ("A.Flurine","B.Francium","C.Iron","D.Fermium"),
           ("A.1910","B.1912","C.1914","D.1920"),
           ("A.Leonardo da vinci","B.Rapheal","C.Michelangelo","D.Donatello"),
           ("A.Jupiter","B.Mars","C.Venus","D.Mecury"))
answers = ("D","C","B","C","B")
guesses =[]
score = 0
question_num = 0

for question in questions:
    print("----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Choose an option( A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print(f"Correct! {answers[question_num]} is right answers")
    else:
        print(f"Incorrect! The right option is {answers[question_num]}")
    input("Continue (Y): ")
    question_num += 1
print("----------------------------")
print("           Results          ")
print("----------------------------")
print("Your Guesses : ", end="")
for guess in guesses:
    print(guess, end="")
print()

print("Right Answers: ",end="")
for answer in answers:
    print(answer, end="")
print()

score = int(score/len(questions)*100)
print (f"Your Score is {score}%")
