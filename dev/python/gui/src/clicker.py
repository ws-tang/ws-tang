"""
Section: 3.1.1.4

Estimated time: 30-45 minutes

Level of difficulty: Medium

Objectives
Learn practical skills related to:
    writing event handlers and assigning them to widgets using the bind() method,
    managing widgets with the grid manager,
    using the after() and after_cancel() methods.

Scenario

We want you to write a simple but challenging game, which can help many people to improve their perception skills and visual memory. We'll call the game The Clicker as clicking is what we expect from the player.

The Clicker's board consists of 25 buttons and each of the buttons contains a random number from range 1..999. Note: each number is different!

Below the board there is a timer which initially shows 0. The timer starts when the user clicks the board for the first time.

Here's how we imagine The Clicker's initial board state:

The Clicker - initial board's state

We expect the player to click all the buttons in the order imposed by the numbers - from the lowest to the highest one. Additional rules say that:

    the properly clicked button changes the button's state to DISABLED (it greys the button out)
    the improperly clicked button shows no activity,
    the timer increases its value every second,
    when all the buttons are greyed out (i.e., the player has completed his/her task) the timer stops immediately.

This is how the board looks when the game is finished:

The Clicker - final board's state

Hint: consider using the <Button-1> event instead of setting the command button property - it may simplify your code.

"""

import tkinter as tk
from random import randint


# Update timer
def update_time():
    elapsed = elapsed_time.get() + 1
    elapsed_time.set(elapsed)
    label["text"] = str(elapsed) + " seconds"
    timer_id.set(label.after(1000, update_time))
    print(f"[update_time] Timer Id [{timer_id.get()}]") 

# Write your code here.
def button_click(event):

    if not timer_init.get():
        timer_id.set(label.after(1000, update_time))
        timer_init.set(True)

    widget = event.widget
    num = int(widget['text'])
    #print(f"List Head {numbers[0]}, button text [{num}]")
    if (numbers[0] == num):
        widget.config(state="disabled")
        del numbers[0]

    if len(numbers) == 0:
        print(f"[button_click] Timer Id [{timer_id.get()}]") 
        label.after_cancel(timer_id.get())

# Window
window = tk.Tk()
window.resizable(False, False)

title = tk.Label(window, text = "Clicker")
title.grid(column=0, row=0, columnspan=5, padx=2, pady=2)

numbers = []

# Buttons 5 x 5
#for i in range (1, 6):
#    for j in range (0, 5):
for i in range (1, 4):
    for j in range (0, 3):
        btn_num = randint(1, 999)
        numbers.append(btn_num)
        button = tk.Button(window, text="{:3d}".format(btn_num))
        button.bind("<Button-1>", button_click)
        button.grid(column=j, row=i, padx=1, pady=1)

numbers.sort()

# Timer
timer_id = None
timer_init = tk.BooleanVar()
timer_init.set(False)
elapsed_time = tk.IntVar()
elapsed_time.set(0)
timer_id = tk.StringVar()

label = tk.Label(window, text = "0 second")
label.grid(column=0, row=6, columnspan=5, padx=2, pady=2)

window.mainloop()
