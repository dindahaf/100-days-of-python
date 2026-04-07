import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# input_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#
# if input_number == 0:
#     user_choice = rock
#     print(rock)
# elif input_number == 1:
#     user_choice = paper
#     print(paper)
# elif input_number == 2:
#     user_choice = scissors
#     print(scissors)
# else:
#     print("Sorry you have to choose from 0 to 2")
#
# list = [rock, paper, scissors]
# computer_choice = random.choice(list)
# print(f"Computer chose: {computer_choice}")
#
# if user_choice == rock and computer_choice == scissors:
#     print("You win!")
# elif user_choice == scissors and computer_choice == paper:
#     print("You win!")
# elif user_choice == paper and computer_choice == rock:
#     print("You win!")
# elif user_choice == computer_choice:
#     print("It's a draw!")
# else:
#     print("You lose :(")

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0,2)
print(f"Computer chose:{game_images[computer_choice]}")

# Define user_choice can not less than 0 and can not more than 2 in the first line so that the code check it first before going down to other codes.
if user_choice >=3 or user_choice < 0:
    print("You type an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")
