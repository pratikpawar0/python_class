import tkinter as tk

# Function to update the input field
def click_button(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Function to evaluate the final expression
def evaluate():
    try:
        global expression
        result = str(eval(expression))  # 'eval' is used to evaluate the string expression
        input_text.set(result)
        expression = result  # Store the result for further calculation
    except:
        input_text.set("Error")
        expression = ""

# Function to clear the input field
def clear_input():
    global expression
    expression = ""
    input_text.set("")

# Initialize window
window = tk.Tk()
window.title("Calculator")
window.geometry("320x400")
window.resizable(0, 0)

# Set window background color
window.configure(bg="lightblue")

expression = ""

# StringVar to store the input and display on the input field
input_text = tk.StringVar()

# Create an input field to display numbers and results
input_frame = tk.Frame(window, bg="lightblue")
input_frame.pack()

input_field = tk.Entry(input_frame, textvariable=input_text, width=50, justify='right', font=('Arial', 18), bg="white", fg="black")
input_field.grid(row=0, column=0)
input_field.pack()

# Create buttons for the calculator
buttons_frame = tk.Frame(window, bg="lightblue")
buttons_frame.pack()

# First row
clear = tk.Button(buttons_frame, text="C", command=clear_input, height=2, width=10, bg="blue", fg="white")
clear.grid(row=0, column=0)

divide = tk.Button(buttons_frame, text="/", command=lambda: click_button("/"), height=2, width=10, bg="blac", fg="white")
divide.grid(row=0, column=1)

multiply = tk.Button(buttons_frame, text="*", command=lambda: click_button("*"), height=2, width=10, bg="orange", fg="white")
multiply.grid(row=0, column=2)

subtract = tk.Button(buttons_frame, text="-", command=lambda: click_button("-"), height=2, width=10, bg="orange", fg="white")
subtract.grid(row=0, column=3)

# Second row
seven = tk.Button(buttons_frame, text="7", command=lambda: click_button(7), height=2, width=10, bg="white", fg="black")
seven.grid(row=1, column=0)

eight = tk.Button(buttons_frame, text="8", command=lambda: click_button(8), height=2, width=10, bg="white", fg="black")
eight.grid(row=1, column=1)

nine = tk.Button(buttons_frame, text="9", command=lambda: click_button(9), height=2, width=10, bg="white", fg="black")
nine.grid(row=1, column=2)

add = tk.Button(buttons_frame, text="+", command=lambda: click_button("+"), height=2, width=10, bg="black", fg="white")
add.grid(row=1, column=3)

# Third row
four = tk.Button(buttons_frame, text="4", command=lambda: click_button(4), height=2, width=10, bg="white", fg="black")
four.grid(row=2, column=0)

five = tk.Button(buttons_frame, text="5", command=lambda: click_button(5), height=2, width=10, bg="white", fg="black")
five.grid(row=2, column=1)

six = tk.Button(buttons_frame, text="6", command=lambda: click_button(6), height=2, width=10, bg="white", fg="black")
six.grid(row=2, column=2)

equal = tk.Button(buttons_frame, text="=", command=evaluate, height=5, width=10, bg="green", fg="white")
equal.grid(row=2, column=3, rowspan=2)

# Fourth row
one = tk.Button(buttons_frame, text="1", command=lambda: click_button(1), height=2, width=10, bg="white", fg="black")
one.grid(row=3, column=0)

two = tk.Button(buttons_frame, text="2", command=lambda: click_button(2), height=2, width=10, bg="white", fg="black")
two.grid(row=3, column=1)

three = tk.Button(buttons_frame, text="3", command=lambda: click_button(3), height=2, width=10, bg="white", fg="black")
three.grid(row=3, column=2)

# Fifth row
zero = tk.Button(buttons_frame, text="0", command=lambda: click_button(0), height=2, width=22, bg="white", fg="black")
zero.grid(row=4, column=0, columnspan=2)

decimal = tk.Button(buttons_frame, text=".", command=lambda: click_button("."), height=2, width=10, bg="white", fg="black")
decimal.grid(row=4, column=2)

# Start the application
window.mainloop()
