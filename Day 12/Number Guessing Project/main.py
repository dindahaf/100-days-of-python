from art import logo
import random

EASY_LEVEL = 10
HARD_LEVEL = 5


# Function set difficulty

def set_difficulty():
    level_chosen = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level_chosen == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


# Function to check users' guess against actual number
# Track the number of turns and reduce by 1 if they get it wrong

def check_answer(user_guess, actual_number, lives):
    """ Checks number again guess, returns the number of lives remaining """
    if user_guess > actual_number:
        print("Too High")
        return lives -1
    elif user_guess < actual_number:
        print("Too low")
        return lives -1
    else:
        print(f"You guessed the number! The answer was {actual_number} ")


# Choosing a random number between 1 and 100
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number_assigned = random.randint(1, 100)
    # print(number_assigned)

    lives = set_difficulty()

    guess = 0
    # Repeat the guessing functionality if they get it wrong
    while guess != number_assigned:
        print(f"You have {lives} attempts remaining to guess the number.")
    # Let the user guess the number
        guess = int(input("Make a guess: "))
        lives = check_answer(guess, number_assigned, lives)
        if lives == 0:
            print(f"You run out of lives!. Your number was {number_assigned}")
            return
        elif guess != number_assigned:
            print("Guess Again!")

game()







