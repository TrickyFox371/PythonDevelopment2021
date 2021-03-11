import tkinter as tk
import random as rnd

from tkinter import messagebox

names = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
window = tk.Tk()
buttons = []
space_row = 0
space_col = 0
frameMenu = tk.Frame(master = window, width = 100, height = 100)
frameMenu.pack()
frameGame = tk.Frame(master = window, width = 100, height = 100)
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
    local_names = names.copy()
    for i in range(0, 16):
        name = local_names[rnd.randrange(0, 16 - i)]
        local_names.remove(name)
        if name == 0:
            space_row = i // 4
            space_col = i % 4
            continue
        button = tk.Button(master = frameGame,
                           height = 10,
                           width = 20,
                           text = str(name))
        button["command"] = Callback(move, button)
        button.grid(row = i // 4, column = i % 4)
        buttons.append(button)

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
