import tkinter as tk
import tkinter.font as font
import random as rnd

from tkinter import messagebox
from random import shuffle

names = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
window = tk.Tk()
buttons = []
space_row = 0
space_col = 0
frameMenu = tk.Frame(master = window)
frameMenu.pack()
frameGame = tk.Frame(master = window)
frameGame.pack()

class Callback:
    def __init__(self, func, button):
        self.func = func
        self.button = button
    def __call__(self):
        self.func(self.button)

def check():
    if space_col != 3 or space_row != 3:
        return False
    for button in buttons:
        info = button.grid_info()
        i = int(button["text"]) - 1
        if info["row"] != i // 4 or info["column"] != i % 4:
            return False
    return True

def move(button):
    global space_row
    global space_col
    info = button.grid_info()
    if (space_row == info["row"] and abs(space_col - info["column"]) == 1) or \
       (space_col == info["column"] and abs(space_row - info["row"]) == 1):
        tmp_row = space_row
        tmp_col = space_col
        space_row = info["row"]
        space_col = info["column"]
        button.grid(row = tmp_row, column = tmp_col)
    if check():
        messagebox.showwarning(title = "win", message = "You win!")
        renew()

def fill():
    global space_col
    global space_row
    shuffle(names)
    i = 0
    for name in names:
        if name == 0:
            space_row = i // 4
            space_col = i % 4
            i += 1
            continue
        button = tk.Button(master = frameGame,
                           height = 10,
                           width = 20,
                           text = str(name))
        button["command"] = Callback(move, button)
        button.grid(row = i // 4, column = i % 4)
        buttons.append(button)
        i += 1

def renew():
    global buttons
    for button in buttons:
        button.grid_remove()
    buttons = []
    fill()

def end():
   window.destroy()


new = tk.Button(master = frameMenu,
                height = 5,
                width = 41,
                text = "New")
new["command"] = renew
new.grid(row = 0, column = 0)
ex = tk.Button(master = frameMenu,
               height = 5,
               width = 41,
               text = "Exit")
ex["command"] = end
ex.grid(row = 0, column = 1)
fill()
print(names)
window.mainloop()
