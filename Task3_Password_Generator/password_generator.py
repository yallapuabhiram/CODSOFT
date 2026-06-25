import tkinter as tk
from tkinter import messagebox
import random
import string

# ---------------- Functions ---------------- #

def generate_password():
    length = length_entry.get()

    if not length.isdigit():
        messagebox.showerror("Error", "Please enter a valid number!")
        return

    length = int(length)

    if length < 4:
        messagebox.showwarning(
            "Warning",
            "Password length should be at least 4!"
        )
        return

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = "".join(
        random.choice(characters)
        for _ in range(length)
    )

    password_var.set(password)


def copy_password():
    password = password_var.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard!"
        )


# ---------------- Main Window ---------------- #

root = tk.Tk()
root.title("Abhiram's Password Generator")
root.geometry("450x300")
root.configure(bg="#121212")
root.resizable(False, False)

# ---------------- Heading ---------------- #

title = tk.Label(
    root,
    text="🔐 PASSWORD GENERATOR",
    font=("Arial", 18, "bold"),
    bg="#121212",
    fg="#00A2FF"
)

title.pack(pady=20)

# ---------------- Length Input ---------------- #

length_label = tk.Label(
    root,
    text="Enter Password Length:",
    font=("Arial", 12),
    bg="#121212",
    fg="white"
)

length_label.pack()

length_entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center",
    width=10,
    bg="#1E1E1E",
    fg="white",
    insertbackground="white"
)

length_entry.pack(pady=10)

# ---------------- Generate Button ---------------- #

generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    bg="#0078D7",
    fg="white",
    command=generate_password,
    width=20,
    bd=0
)

generate_btn.pack(pady=15)

# ---------------- Password Display ---------------- #

password_var = tk.StringVar()

password_entry = tk.Entry(
    root,
    textvariable=password_var,
    font=("Consolas", 14),
    justify="center",
    width=30,
    bg="#1E1E1E",
    fg="#00FF7F",
    insertbackground="white"
)

password_entry.pack(pady=10)

# ---------------- Copy Button ---------------- #

copy_btn = tk.Button(
    root,
    text="Copy Password",
    font=("Arial", 12, "bold"),
    bg="#0078D7",
    fg="white",
    command=copy_password,
    width=20,
    bd=0
)

copy_btn.pack(pady=10)

root.mainloop()
