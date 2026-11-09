import random
score = 0
while True:
    print("\nChoose Difficulty")
    print("1.Easy(10 guesses)")
    print("2.Medium(7 guesses)")
    print("3.Hard(5 guesses)")
    choice = input("Choose Difficulty: ")
    if choice == "1":
        attempts = 10
    elif choice == "2":
        attempts = 7
    elif choice == "3":
        attempts = 5
    else:
        print("Invalid Choice")
        continue
    secret = random.randint(1, 100)
    guesses = 0
    while guesses < attempts:
        guess = input("Enter Your Guess: ")
        if not guess.isdigit():
            print("Numbers Only.")
            continue
        guess = int(guess)
        guesses += 1
        if guess < 1 or guess > 100:
            print("Enter A Number Between 1 and 100")
            continue
        if guess == secret:
            print("Congratulation You Guessed Correctly.")
            if guesses == 1:
                score += 3
            elif guesses == 2:
                score += 2
            elif guesses == 3:
                score += 1
            print(f"You Used {guesses} guess(es).")
            break
        elif guess < secret:
            print("Too Low!")
        else:
            print("Too High")
        print(f"Remaining guesses: {attempts - guesses}")
    else:
        print("You Lost.")
        print("The Number was", secret)
    print("Current Score",score)
    again = input("Play Again? (yes/no)").lower()
    if again != "yes":
        break
    print("\nFinal Score:", score)
    print("Thanks For Playing!") 