# import logo, data and import random module for applying at calling the random list
import random
from art import logo, vs
from game_data import data

# Computer fetch the list based on random choice, two times and displaying to the user the key of name, description,country
def print_key(assigned_data):
    return f"{assigned_data['name']}, a {assigned_data['description']}, from {assigned_data['country']}"

# Assigning the fetch_data1 to A and fetch_data2 to B (No need)

# Computer evaluate which one has bigger follower between A and B
# Computer perform to choose whether the user answer is right or wrong, doing the things based on the answer afterward
# if the user's answer is right then adding the score and assign the right list to the next game

def compare(data1, data2, user_answer):
    if data1['follower_count'] > data2['follower_count']:
        return user_answer == "A" # This will return True if this condition happens and user choose A
    else:
        return user_answer == "B" # This will return False

# if the answer is always right then the game will never stop. Doing the same thing again and again
# if the user's answer is wrong then stop the program and displaying the final score

# there is a rule for adding the score or displaying the final score
print(logo)
score = 0
game_should_continue = True
fetch_data2 = random.choice(data)

while game_should_continue:

    # write codes of random list and assign to a variable
    # Making account at position B become the next at position A
    fetch_data1 = fetch_data2
    fetch_data2 = random.choice(data)

    if fetch_data1 == fetch_data2:
        fetch_data2 = random.choice(data)

    # Showing the two sides of comparison: A and B
    print(f"Compare A: {print_key(fetch_data1)}")
    print(vs)
    print(f"Against B: {print_key(fetch_data2)}")

    # Asking the user to choose which is A or B
    answer = input("Who has more followers? Type A and B: ").upper()

    # Clear the screen
    print("\n" * 20)
    print(logo)

    is_correct = compare(fetch_data1, fetch_data2, answer)
    if is_correct:
        # Adding the score
        score += 1
        # Give user feedback on their guess
        print(f"You're right. Your current score is {score}")
    else:
        print(f"You chose the wrong answer. Your final score is {score}")
        game_should_continue = False








