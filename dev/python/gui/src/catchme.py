"""
Section: 3.1.1.3

Estimated time: 20-30 minutes

Level of difficulty: Easy

Objectives
    Learn practical skills related to:

        using screen coordinates,
        managing widgets with the place manager,
        binding events using the bind() method.


Scenario
    Write a simple game - an infinite game which humans cannot win. Here are the rules:

        the game goes on between TkInter and the user (probably you)
        TkInter opens a 500x500 pixel window and places a button saying "Catch me!" in the top-left corner of the window;
        if the user moves the mouse cursor over the button, the button immediately jumps to another location inside the window; you have to assure that the new location is distant enough to prevent the user from making an instant click,
        the button must not cross the window's boundaries during the jump!

Here is a sample picture for your reference:

Catch me if you can - reference

Use the place() method to move the button, and the bind() method to assign your own callback.

"""

import tkinter as tk
from tkinter import messagebox
import random


# Write your code here.
def jump_on_movein(event=None):
    if event is None:
        tk.messagebox.showinfo("Mouse In!", "......")
        return

    x_right_boundary = 500 - button.winfo_width() - 10;
    btn_x = button.winfo_x() + random.randint(0, 500)
    if btn_x > x_right_boundary:
        btn_x -= 500
        if btn_x < 0:
            btn_x = random.randint(0, 250)
    y_bottom_boundary = 500 - button.winfo_height() - 10;
    btn_y = button.winfo_y() + random.randint(0, 500)
    if btn_y > y_bottom_boundary:
        btn_y -= 500
        if btn_y < 0:
            btn_y = random.randint(0, 250)

    button.place(x=btn_x, y=btn_y)


# Window
window = tk.Tk()
window.title("Catch Me")
window.geometry("500x500")
window.resizable(False, False)
window.configure(bg="white")

# Button
button = tk.Button(window, text="Catch Me!", command=window.destroy)
button.bind("<Enter>", jump_on_movein)
button.pack()
button.place(x=window.winfo_x()+20, y=window.winfo_y()+40)

window.mainloop()
