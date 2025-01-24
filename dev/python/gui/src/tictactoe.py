"""
Section: 3.1.1.6

Estimated time: 30-45 minutes

Level of difficulty: Hard

Objectives
Learn practical skills related to:

    dealing with the grid geometry manager,
    defining and using callbacks,
    identifying and servicing GUI events.

Scenario
Write a simple GUI program which pretends to play tic-tac-toe with the user. Don't be afraid, we don't want you to implement artificial intelligence algorithms. You can do it, if you want, but we prefer to concentrate on the user interface issues. If you really want to create an actual competitor, do it on your own.

This is what the game you are about to write looks like (the beginning and sample end of the game):

ttt-start

ttt-finish

To make your task a bit easier, let's simplify the game a bit. Here are our assumptions:.

    the computer (i.e., your program) plays 'X', and Xes are always red,
    the user (e.g., you) plays 'O', and Os are always green,
    the board consists of 9 tiles, and the tile role is played by a button,
    the first move belongs to the computer - it always puts its first 'X' in the middle of the board,
    the user enters her/his move by clicking the chosen tile (clicking the tiles which are not free is ineffective)
    the program checks if the game over conditions are met, and if the game is over, a message box is displayed announcing the winner,
    otherwise the computer responds with its move and the check is repeated,
    use random to generate the computer's moves.

"""

import tkinter as tk
from random import randint
from tkinter import messagebox, font


# Check if start the game again
def start_over():
    answer = messagebox.askquestion("Tic Tac Toe", "Do you want to play again?")
    if answer == "no":
        window.destroy();
 
    # Start over the game
    for i in range (9):
        button = buttons[i]
        text = button["text"]
        if text != "":
            button["text"] = ""

# Check cell selections
def check_cell_selections():
    is_all_set = True
    for i in range (9):
        button = buttons[i]
        if button["text"] == "":
            is_all_set = False
            break

    if is_all_set:
        messagebox.showinfo("Game Result", "All cells are set. It is a tie!!")

    return is_all_set

# Check the game status
def check_result():
    btn_texts = [""] * 9
    for i in range (9):
        button = buttons[i]
        btn_texts[i] = button["text"]

    #print(btn_texts)

    # Check the lines 0-1-2, 0-3-6, 0-4-8
    if btn_texts[0] != "":
        if btn_texts[0] == btn_texts[1] and btn_texts[1] == btn_texts[2]:
            return True
        if btn_texts[0] == btn_texts[3] and btn_texts[3] == btn_texts[6]:
            return True
        if btn_texts[0] == btn_texts[4] and btn_texts[4] == btn_texts[8]:
            return True

    # Check the lines 2-5-8, 2-4-6
    if btn_texts[2] != "":
        if btn_texts[2] == btn_texts[5] and btn_texts[5] == btn_texts[8]:
            return True
        if btn_texts[2] == btn_texts[4] and btn_texts[4] == btn_texts[8]:
            return True

    # Check the lines 1-4-7
    if btn_texts[1] != "":
        if btn_texts[1] == btn_texts[4] and btn_texts[4] == btn_texts[7]:
            return True

    # Check the lines 3-4-5
    if btn_texts[3] != "":
        if btn_texts[3] == btn_texts[4] and btn_texts[4] == btn_texts[5]:
            return True

    # Check the lines 6-7-8
    if btn_texts[6] != "":
        if btn_texts[6] == btn_texts[7] and btn_texts[7] == btn_texts[8]:
            return True

    return False

def do_computer_move():
    computer_move_done = False
    counter = 0
    while counter < 9:
        selected_idx = randint(0, 8)
        button = buttons[selected_idx]
        counter += 1
        if button["text"] == "":
            print(f"Selected Index [{selected_idx}]")
            button.config(text="X")
            button.config(state="disabled")
            computer_move_done = True
            break

    # random move does not work... manual move now
    if not computer_move_done:
        print("Random computer move failed...")
        for i in range (9):
            button = buttons[i]
            if button["text"] == "":
                button.config(text="X")
                button.config(state="disabled")
                widget.config(fg="red")
                break

    if check_result():
        messagebox.showinfo("Game Result", "The computer has won!!")
        start_over()

    if check_cell_selections():
        start_over()

# Write your code here.
def button_click(event):
    widget = event.widget
    btn_text = widget['text']
    
    if btn_text != "":
        return

    widget.config(text="O")
    widget.config(state="disabled")
    widget.config(fg="blue")

    if check_result():
        messagebox.showinfo("Game Result", "Congratulations!! You won!!")
        start_over()
    elif check_cell_selections():
        start_over()
    else:
        do_computer_move()

# Main routine
window = tk.Tk()
window.resizable(False, False)

title = tk.Label(window, text = "Tic-Tac-Toe")
title.grid(column=0, row=0, columnspan=5, padx=2, pady=2)

buttons = [None] * 9

# Buttons 3 x 3
button_font = font.Font(family="Helvetica", size=16, weight="bold")
for i in range (3):
    for j in range (3):
        button = tk.Button(window, text="", font=button_font)
        button.bind("<Button-1>", button_click)
        button.config(width=15,height=2)
        button.grid(column=j, row=i+1, padx=1, pady=1)
        buttons[i * 3 + j] = button

window.mainloop()
