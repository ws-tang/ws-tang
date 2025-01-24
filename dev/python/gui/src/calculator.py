"""
Section: 3.1.1.2

Estimated time: 20-30 minutes

Level of difficulty: Easy

Objectives
Learn practical skills related to:

    using the Entry, Radiobutton and Button widgets,
    managing widgets with the grid manager,
    checking the validity of user input and handling errors.

Scenario
You need a calculator. A very simple and very specific calculator. Look at the picture - it contains two fields that the user can use to enter arguments, a radio button to select the operation to perform, and a button initiating the evaluation:

Calculator - reference

We expect the calculator to behave in the following way:

    if both fields contain valid (integer or float) numbers, clicking the Evaluate button should display an info window showing the evaluation's result;
    if any of the fields contains invalid data (e.g., a string, or a field is empty), clicking the Evaluate button should present an error window describing the problem, and the focus should be moved to the field causing the problem.

Don't forget to protect your code from dividing by zero, and use the grid manager to compose the window interior.

"""

import tkinter
from tkinter import messagebox


def evaluate():
    input1 = entry1.get()
    input2 = entry2.get()
    try:
        value1 = int(input1)
        value2 = int(input2)
    except ValueError:
        try:
            value1 = float(input1)
            value2 = float(input2)
        except ValueError:
            messagebox.showerror("Error", "Invalid number(s)!")
            return

    print(f"[Value 1 [{value1}], Value 2 [{value2}]")
    op = selected_op.get()
    print(f"[evaluate]. Operation index is [{op}]")
    if op == 0:    # Addition
        messagebox.showinfo("Addition", "{} + {} = {}".format(value1, value2, str(value1 + value2)))
    elif op == 1:    # Substraction
        messagebox.showinfo("Substraction", "{} - {} = {}".format(value1, value2, str(value1 - value2)))
    elif op == 2:    # Multiplication
        messagebox.showinfo("Multiplication", "{} x {} = {}".format(value1, value2, str(value1 * value2)))
    elif op == 3:    # Division
        if value2 == 0 or value2 == 0.0:
            messagebox.showerror("Error", "Cannot divide by zero!")
        else:
            messagebox.showinfo("Division", "{} / {} = {}".format(value1, value2, str(value1 / value2)))
    else:
        messagebox.showerror("Error", "Invalid calulation operation!")


# Main routine
window = tkinter.Tk()
window.title("Calculator")

# Entries
entry1 = tkinter.Entry(window, width=30)
entry1.grid(column=0, row=2, padx=5, pady=5)
entry2 = tkinter.Entry(window, width=30)
entry2.grid(column=2, row=2, padx=5, pady=5)

# radiobuttons
selected_op = tkinter.IntVar()

rb_plus = tkinter.Radiobutton(window, text="+", variable=selected_op, value=0)
rb_plus.grid(column=1, row=0, padx=5, pady=5)
rb_plus.select()
rb_minus = tkinter.Radiobutton(window, text="-", variable=selected_op, value=1)
rb_minus.grid(column=1, row=1, padx=5, pady=5)
rb_multi = tkinter.Radiobutton(window, text="*", variable=selected_op, value=2)
rb_multi.grid(column=1, row=2, padx=5, pady=5)
rb_div = tkinter.Radiobutton(window, text="/", variable=selected_op, value=3)
rb_div.grid(column=1, row=3, padx=5, pady=5)

# button
btn_eval = tkinter.Button(window, text ="Evaludate", command=evaluate)
btn_eval.grid(column=1, row=4, padx=5, pady=5)

window.mainloop()
