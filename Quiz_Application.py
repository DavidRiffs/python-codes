questions = ["What is the capital of nigeria?",
             "What keyword is used to creat a loop that repeats while a condition is true?",
             "Which function is used to get the legnth of a list?"]
answers = ["Abuja",
           "while",
           "len"]
score = 0
correct_count = 0
wrong_count = 0
wrong_answers = []
while answers:
        print("Welcome To Our Quiz")
        print("please Choose The Correct Answer For Each Questions")
        for question, answer in zip(questions, answers):
                input(question)
                user_answer = input("Your Answer: ")
                if user_answer.strip().lower() == answer.lower():
                    print("Correct")
                    score += 1
                    correct_count += 1
                else:
                     wrong_count += 1
                     print("Wrong: The Correct Answer is", {answer})
                     wrong_answers.append((question, answer))
                     print(f"Your current Score is: {score}")
        print("Quiz completed")
        print(f"Correct Answers are:", correct_count)
        print(f"Wrong Answers are:", wrong_count)
        print(f"\n Your Final Score is: {score}/{len(questions)}")

        review = input("Would You Like To Review Wrong Answers?(yes/no: )")
        if review == "yes":
            for question, answer in wrong_answers:
                print(f"Wrong Answers:",question)
                print(f"Correct Answers:",answer)
                print()
        else:
            again = input("Would You Like To Play Again?(yes/no): ")
            if again != "yes":
                break