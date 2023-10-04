import random

print("Welcome to the number guessing game")
print("I am thinking of a number from 1 - 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

print(f"Attempts: {attempts}")

still_playing = True
number = random.randint(1, 100)

while still_playing:
    if attempts > 0:
        print(f"You have {attempts} left to guess the number")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}")
            still_playing = False
        elif guess < number:
            print("Too low. Guess Again")
            attempts -= 1
        elif guess > number:
            print("Too high. Guess Again")
            attempts -= 1
    else:
        print(f"You ran out of guesses! The number was {number}")
        still_playing = False
