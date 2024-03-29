# Rock-Paper-Scissors game

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

#Write your code below this line 👇
print("Let's play Rock, Paper, Scissors!")

game_options = ['rock', 'paper', 'scissors']

user_choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))
print("You Chose:")
print(game_options[user_choice])

computer_choice = random.randint(0, 2)
print("Computer Chose:")
print(game_options[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("Invalid choice. You Lose.")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose.")
elif computer_choice > user_choice:
    print("You Lose.")
elif computer_choice < user_choice:
    print("You Win!")
elif user_choice == computer_choice:
    print("It's a tie.")
