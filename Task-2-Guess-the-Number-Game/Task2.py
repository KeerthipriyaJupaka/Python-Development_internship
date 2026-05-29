import random

print("===================================")
print("     GUESS THE NUMBER GAME")
print("===================================")

# Generate random number
secret_number = random.randint(1, 100)

attempts = 0

print("\nI have selected a number between 1 and 100.")
print("Try to guess it!\n")

while True:
    try:
        # User input
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Compare guess with secret number
        if guess < secret_number:
            print("Too Low! Try again.\n")

        elif guess > secret_number:
            print("Too High! Try again.\n")

        else:
            print("\n🎉 Congratulations! You guessed the number correctly.")
            print(f"You guessed it in {attempts} attempts.")
            break

    except ValueError:
        print("Invalid input! Please enter a valid number.\n")

print("\nThank you for playing the game!")
