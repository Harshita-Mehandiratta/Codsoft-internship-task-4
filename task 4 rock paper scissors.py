#!/usr/bin/env python
# coding: utf-8

# In[2]:


#task 4 rock paper scissors game
import random

# Define the choices for the game
choices = ["rock", "paper", "scissors"]

# Function to get the user's choice
def get_user_choice():
    while True:
        print("Choose one:")
        for i, choice in enumerate(choices):
            print(f"{i}. {choice}")
        
        try:
            user_choice = int(input("Enter the number of your choice: "))
            if user_choice >= 0 and user_choice < len(choices):
                return user_choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to get the computer's choice
def get_computer_choice():
    return random.randint(0, 2)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        return "Congratulations! You win!"
    else:
        return "Sorry, you lose."

# Main game loop
while True:
    print("Welcome to Rock-Paper-Scissors!")
    
    user_choice = get_user_choice()
    print(f"You chose: {choices[user_choice]}")

    computer_choice = get_computer_choice()
    print(f"Computer chose: {choices[computer_choice]}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thank you for playing! Goodbye!")
        break


# In[ ]:




