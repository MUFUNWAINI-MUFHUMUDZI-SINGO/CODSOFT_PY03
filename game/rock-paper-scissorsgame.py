import tkinter as tk
import random

# Dictionary to map choices to integers
choices = {0: "Rock", 1: "Paper", 2: "Scissors"}

# Function to determine winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle user input and game logic
def play_game(user_choice):
    computer_choice = random.choice(list(choices.values()))
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Create main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.configure(bg="#f0f0f0")  # Set background color

# Title label with colorful text
title_label = tk.Label(root, text="Rock-Paper-Scissors Game", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333333")
title_label.pack(pady=10)

# Frame for buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

# Function to create and style buttons with different colors
def create_button(text, color):
    return tk.Button(button_frame, text=text, width=10, height=2, font=("Arial", 12),
                     command=lambda: play_game(text), bg=color, fg="#ffffff")

# Buttons for user choices with different colors
rock_button = create_button("Rock", "#3498db")  # Blue color
rock_button.grid(row=0, column=0, padx=10)

paper_button = create_button("Paper", "#2ecc71")  # Green color
paper_button.grid(row=0, column=1, padx=10)

scissors_button = create_button("Scissors", "#e74c3c")  # Red color
scissors_button.grid(row=0, column=2, padx=10)

# Label to display result with a colorful background
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#ffffff", fg="#333333", padx=20, pady=10, relief=tk.RIDGE)
result_label.pack(pady=20)

# Run the application
root.mainloop()
