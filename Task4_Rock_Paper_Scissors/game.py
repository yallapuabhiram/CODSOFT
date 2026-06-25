import tkinter as tk
import random


# Scores
user_score = 0
computer_score = 0


# Game Logic
def play(user_choice):
    global user_score, computer_score

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    user_label.config(text=f"You: {user_choice}")
    computer_label.config(text=f"Computer: {computer_choice}")

    if user_choice == computer_choice:
        result = "🤝 It's a Draw!"

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        user_score += 1
        result = "🎉 You Win!"

    else:
        computer_score += 1
        result = "😢 Computer Wins!"

    result_label.config(text=result)
    score_label.config(
        text=f"Your Score: {user_score}   Computer: {computer_score}"
    )


# Reset Scores
def reset_game():
    global user_score, computer_score

    user_score = 0
    computer_score = 0

    score_label.config(
        text="Your Score: 0   Computer: 0"
    )

    user_label.config(text="You: -")
    computer_label.config(text="Computer: -")
    result_label.config(text="Choose an option!")


# Main Window
root = tk.Tk()
root.title("Abhiram's Rock Paper Scissors")
root.geometry("500x400")
root.configure(bg="#121212")
root.resizable(False, False)


# Title
title = tk.Label(
    root,
    text="🎮 ROCK PAPER SCISSORS",
    font=("Arial", 18, "bold"),
    bg="#121212",
    fg="#00A2FF"
)

title.pack(pady=20)


# Score
score_label = tk.Label(
    root,
    text="Your Score: 0   Computer: 0",
    font=("Arial", 14),
    bg="#121212",
    fg="white"
)

score_label.pack(pady=10)


# Buttons
button_frame = tk.Frame(root, bg="#121212")
button_frame.pack(pady=20)

button_style = {
    "font": ("Arial", 12, "bold"),
    "bg": "#0078D7",
    "fg": "white",
    "width": 10,
    "bd": 0
}

tk.Button(
    button_frame,
    text="🪨 Rock",
    command=lambda: play("Rock"),
    **button_style
).grid(row=0, column=0, padx=10)

tk.Button(
    button_frame,
    text="📄 Paper",
    command=lambda: play("Paper"),
    **button_style
).grid(row=0, column=1, padx=10)

tk.Button(
    button_frame,
    text="✂️ Scissors",
    command=lambda: play("Scissors"),
    **button_style
).grid(row=0, column=2, padx=10)


# Result Labels
user_label = tk.Label(
    root,
    text="You: -",
    font=("Arial", 14),
    bg="#121212",
    fg="white"
)

user_label.pack(pady=5)


computer_label = tk.Label(
    root,
    text="Computer: -",
    font=("Arial", 14),
    bg="#121212",
    fg="white"
)

computer_label.pack(pady=5)


result_label = tk.Label(
    root,
    text="Choose an option!",
    font=("Arial", 16, "bold"),
    bg="#121212",
    fg="#00FF7F"
)

result_label.pack(pady=20)


# Reset Button
tk.Button(
    root,
    text="Reset Game",
    command=reset_game,
    font=("Arial", 12, "bold"),
    bg="#0078D7",
    fg="white",
    width=15,
    bd=0
).pack()


root.mainloop()
