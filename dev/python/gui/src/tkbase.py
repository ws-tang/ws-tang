"""
Section: 1.2.1.3

"""

""" Example 1
import tkinter
from tkinter import messagebox


def Click():
    replay = messagebox.askquestion("Quit?", "Are you sure?")
    if replay == 'yes':
        skylight.destroy();


skylight = tkinter.Tk()
skylight.title("Skylight")
button = tkinter.Button(skylight, text="Bye!", command=Click)
button.place(x=10, y=10)
skylight.mainloop()
"""

""" Example 2
import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text="Little label:")
label.pack()

frame = tk.Frame(window, height=30, width=100, bg="#000099")
frame.pack()

button = tk.Button(window, text ="Button")
button.pack(fill=tk.X)

switch = tk.IntVar()
switch.set(1)

checkbutton = tk.Checkbutton(window, text="Check Button", variable=switch)
checkbutton.pack()

entry = tk.Entry(window, width=30)
entry.pack()

switch2 = tk.IntVar()
switch2.set(1)

radiobutton_1 = tk.Radiobutton(window, text="Steak", variable=switch2, value=0)
radiobutton_1.pack()
radiobutton_2 = tk.Radiobutton(window, text="Salad", variable=switch2, value=1)
radiobutton_2.pack()

window.mainloop()
"""


""" Example 3
import tkinter as tk


def on_off():
    global button
    state = button["text"]
    if state == "ON":
        state = "OFF"
    else:
        state = "ON"
    button["text"] = state


window = tk.Tk()
button = tk.Button(window, text="OFF", command=on_off)
button.place(x=50, y=100, width=100)
window.mainloop()
"""

""" Example 4
import tkinter as tk


def r_observer(*args):
    print("Reading")


def w_observer(*args):
    print("Writing")


dummy = tk.Tk()    # we need this although we won't display any windows
variable = tk.StringVar()
print("1")
variable.set("abc")
print("2")
r_obsid = variable.trace("r", r_observer)
print("3")
w_obsid = variable.trace("w", w_observer)
print("4")
variable.set(variable.get() + 'd')  # read followed by write
print("5")
variable.trace_vdelete("r", r_obsid)
print("6")
variable.set(variable.get() + 'e')
print("7")
variable.trace_vdelete("w", w_obsid)
print("8")
variable.set(variable.get() + 'f')
print("9")
print(variable.get())
"""


import tkinter as tk

window = tk.Tk()
window.maxsize(width=500, height=300)
window.geometry("200x200")
window.mainloop()
