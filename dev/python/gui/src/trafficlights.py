"""
Section: 3.1.1.5

Estimated time: 20-30 minutes

Level of difficulty: Easy

Objectives
Learn practical skills related to:

    dealing with Canvas and some of its methods,
    using different colors.

Scenario
Look at the snippet in the editor - can you see that mysterious tuple consisting of four three-element tuples? Can you guess what information it carries?

It's a set of rules describing the behavior of British-style traffic lights. Assume that the very first element of all inner tuples is assigned to the red light, the second - to the yellow, and the third - to the green one. True means that the light is on, False - off.

As you see, there are four different phases:

    the red light is lit,
    the red and yellow lights are lit together,
    the green light is lit,
    the yellow light is lit.

Your task is to implement a model which will show how such a traffic signal works. The model should look as follows:

Red Red-Yellow Green Yellow

As you see, the model is built of three widgets:

    the canvas being a background for all the three lights,
    the button named "Next" - clicking it switches the signal to the next phase,
    the button named "Quit" - clicking it immediately exits the program.

Note: use the phases tuple as a "knowledge base" for your whole code. The code has to adopt to any change done to the tuple, e.g., there can be more or less than four phases and the lights' combinations can be different also.

If traffic lights in your home country work in a different way, you can implement your native scheme, but the only change you're allowed to make is to modify the phases tuple - the code itself must remain the same.

"""

import tkinter as tk


phases = ((True,  False, False),
          (True,  True,  False),
          (False, False, True),
          (False, True,  False))


# Write your code here.
def handle_next():
    phase_idx = current_idx.get() + 1
    if phase_idx > 3:
        phase_idx = 0

    modes = phases[phase_idx]
    if modes[0]:
        canvas.itemconfig(red_circle, fill= "red")
    else:
        canvas.itemconfig(red_circle, fill= "grey")

    if modes[1]:
        canvas.itemconfig(yellow_circle, fill= "yellow")
    else:
        canvas.itemconfig(yellow_circle, fill= "grey")

    if modes[2]:
        canvas.itemconfig(green_circle, fill= "green")
    else:
        canvas.itemconfig(green_circle, fill= "grey")

    current_idx.set(phase_idx)

# Window
window = tk.Tk()
window.resizable(False, False)

canvas_width = 200
canvas_height = 500
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="grey")
canvas.pack()

# Define circle parameters
radius = 50
x0 = 50
x1 = 150

# Circles
center_y = 75
red_circle_y0 = center_y - radius
red_circle_y1 = center_y + radius
red_circle = canvas.create_oval(x0, red_circle_y0, x1, red_circle_y1,
                                fill="red", outline="black", width=2)

center_y = 200
yellow_circle_y0 = center_y - radius
yellow_circle_y1 = center_y + radius
yellow_circle = canvas.create_oval(x0, yellow_circle_y0, x1,
                                   yellow_circle_y1, fill="grey",
                                   outline="black", width=2)

center_y = 325
green_circle_y0 = center_y - radius
green_circle_y1 = center_y + radius
green_circle = canvas.create_oval(x0, green_circle_y0, x1, green_circle_y1,
                                  fill="grey", outline="black", width=2)

button_next = tk.Button(window, text="Next", command=handle_next)
button_next.pack()
button_next.config(width=8, height=1)
button_next.place(x=70, y=420)

button_quit = tk.Button(window, text="Quit", command=window.destroy)
button_quit.pack()
button_quit.config(width=8, height=1)
button_quit.place(x=70, y=450)

current_idx = tk.IntVar()
current_idx.set(0)

window.mainloop()
