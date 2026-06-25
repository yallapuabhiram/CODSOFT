import tkinter as tk

# Main Window
root = tk.Tk()
root.title("Abhiram's Smart Calculator")
root.geometry("350x500")
root.configure(bg="#121212")
root.resizable(False, False)

expression = ""


# Functions
def press(value):
    global expression
    expression += str(value)
    equation.set(expression)


def calculate():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)


# Display
equation = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=equation,
    font=("Arial", 28),
    bg="#1E1E1E",
    fg="white",
    bd=0,
    justify="right",
    insertbackground="white"
)

display.grid(row=0, column=0, columnspan=4,
             ipadx=8, ipady=25, padx=10, pady=20, sticky="nsew")


# Button Style
number_bg = "#2D2D2D"
operator_bg = "#0078D7"

button_font = ("Arial", 16, "bold")


# Buttons
buttons = [
    ("C", 1, 0, clear, operator_bg),
    ("⌫", 1, 1, backspace, operator_bg),
    ("%", 1, 2, lambda: press("%"), operator_bg),
    ("/", 1, 3, lambda: press("/"), operator_bg),

    ("7", 2, 0, lambda: press("7"), number_bg),
    ("8", 2, 1, lambda: press("8"), number_bg),
    ("9", 2, 2, lambda: press("9"), number_bg),
    ("*", 2, 3, lambda: press("*"), operator_bg),

    ("4", 3, 0, lambda: press("4"), number_bg),
    ("5", 3, 1, lambda: press("5"), number_bg),
    ("6", 3, 2, lambda: press("6"), number_bg),
    ("-", 3, 3, lambda: press("-"), operator_bg),

    ("1", 4, 0, lambda: press("1"), number_bg),
    ("2", 4, 1, lambda: press("2"), number_bg),
    ("3", 4, 2, lambda: press("3"), number_bg),
    ("+", 4, 3, lambda: press("+"), operator_bg),

    ("0", 5, 0, lambda: press("0"), number_bg),
    (".", 5, 1, lambda: press("."), number_bg),
    ("=", 5, 2, calculate, "#005BBB"),
]


# Create Buttons
for text, row, col, command, color in buttons:

    if text == "=":
        btn = tk.Button(
            root,
            text=text,
            command=command,
            font=button_font,
            bg=color,
            fg="white",
            bd=0,
            activebackground="#3399FF",
            activeforeground="white"
        )

        btn.grid(
            row=row,
            column=col,
            columnspan=2,
            sticky="nsew",
            padx=5,
            pady=5
        )

    else:
        btn = tk.Button(
            root,
            text=text,
            command=command,
            font=button_font,
            bg=color,
            fg="white",
            bd=0,
            activebackground="#3399FF",
            activeforeground="white"
        )

        btn.grid(
            row=row,
            column=col,
            sticky="nsew",
            padx=5,
            pady=5
        )


# Grid Configuration
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)


root.mainloop()
