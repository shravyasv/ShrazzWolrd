import random

print("🎮 Number Guessing Puzzle Game")
print("Guess a number between 1 and 100")

secret = random.randint(1, 100)

while True:
    guess = int(input("Enter your guess: "))
    difference = abs(secret-guess)

    if guess == secret:
        print("🎉 Congratulations! You guessed correctly.")
        break

    elif difference <= 2:
        print("🔥 Very Close!")

    elif difference <= 10:
        if guess < secret:
            print("⬆ Low but Close!")
        else:
            print("⬇ High but Close!")

    else:
        if guess < secret:
            print("⬆ Too Low!")
        else:
            print("⬇ Too High!")