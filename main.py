#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
import time
from art import logo

logos = random.choice(logo)
print(logos)
time.sleep(1.5)
random_number = random.randint(1, 100)


def guess(chances):
    answer = False
    for i in range(chances, 0, -1):  #for i in reversed(range(choice))
        time.sleep(0.5)
        print(f"You have {i} attempts remaining to guess the number.")
        time.sleep(0.75)
        user_guess = int(input("Make a guess:"))
        if user_guess == random_number:
            print(f"You got it! The answer was {random_number}")
            answer = True
            break
        elif user_guess > random_number:
            time.sleep(0.25)
            print("Too High.")
        else:
            time.sleep(0.25)
            print("Too Low.")
    if answer == False:
        time.sleep(0.75)
        print(f"Sorry, Better luck next time. The number was {random_number}")


print("Welcome to the Number Guessing Game!")
time.sleep(1)
print("I'm thinking of a number between 1 and 100.")
time.sleep(1)
choice = input("Choose a difficulty (easy/normal/hard): ")
time.sleep(1)
difficulty = {"easy": 10, "medium": 7, "hard": 5}
guess(difficulty[choice])
