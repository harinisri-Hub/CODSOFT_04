import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

# Function to handle the user's choice
def user_choice(choice):
    global user_score, computer_score
    user_choice_label.config(text=f"Your choice: {choice.capitalize()}")
    
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    computer_choice_label.config(text=f"Computer's choice: {computer_choice.capitalize()}")
    
    result = determine_winner(choice, computer_choice)
    result_label.config(text=result)
    
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1
    
    score_label.config(text=f"Score - You: {user_score}  Computer: {computer_score}")

# Function to reset the game
def reset_game():
    user_choice_label.config(text="Your choice:")
    computer_choice_label.config(text="Computer's choice:")
    result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

user_score = 0
computer_score = 0

# Create and place the widgets
instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
instruction_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button_rock = tk.Button(root, text="Rock", command=lambda: user_choice('rock'))
button_rock.grid(row=1, column=0, padx=10, pady=10)

button_paper = tk.Button(root, text="Paper", command=lambda: user_choice('paper'))
button_paper.grid(row=1, column=1, padx=10, pady=10)

button_scissors = tk.Button(root, text="Scissors", command=lambda: user_choice('scissors'))
button_scissors.grid(row=1, column=2, padx=10, pady=10)

user_choice_label = tk.Label(root, text="Your choice:")
user_choice_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

computer_choice_label = tk.Label(root, text="Computer's choice:")
computer_choice_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

score_label = tk.Label(root, text=f"Score - You: {user_score}  Computer: {computer_score}")
score_label.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

reset_button = tk.Button(root, text="Play Again", command=reset_game)
reset_button.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

# Run the application
root.mainloop()
