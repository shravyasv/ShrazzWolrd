import random

print("🎮 Welcome to AnkeMystery 🎮")
print("..Guess and Win..🏆" )
while True:

    print("\nChoose a Level")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-500)")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        limit = 50
    elif choice == "2":
        limit = 100
    elif choice == "3":
        limit = 500
    else:
        print("Invalid choice! Medium selected.")
        limit = 100

    secret = random.randint(1, limit)

    print(f"\nGuess a number between 1 and {limit}")

    # Hint only once
    if secret % 2 == 0:
        print("💡 Hint: Number is Even")
    else:
        print("💡 Hint: Number is Odd")

    attempts = 0
    history = []

    while True:

        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("❌ Enter numbers only.")
            continue

        attempts += 1
        history.append(guess)

        diff = abs(secret - guess)

        if guess == secret:
            print("\n🎉 Congratulations!")
            print(f"✅ Correct Number: {secret}")
            print(f"🏆 Attempts: {attempts}")
            print("📜 Your Guesses:", history)
            break

        if guess < secret:
            print("⬆️ Low but....")
        else:
            print("⬇️ High but....")

        # Hot & Cold hints
        if diff <= 3:
            print("🔥 Very Close!")
        elif diff <= 10:
            print("😊 Close!")
        elif diff <= 20:
            print("🙂 You are Near But Not Close !")
        else:
            print("❄️ Far Away!")

        print("📜Your History:", history)

    again = input("\nPlay Again? (yes/no): ").lower()

    if again != "yes":
        print("\n👋 Thank You! Have a Good Day!")
        break