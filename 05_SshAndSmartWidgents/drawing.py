import tkinter as tk
import inspect

class TextWindow(tk.Frame):
    def __init__(self, master = None, title = "<application>", **kwargs):
        super().__init__(master, **kwargs)
        self.master.title(title)

class GraphicsWindow(tk.Frame):
    def __init__(self, master = None, title = "<application>", **kwargs):
        super().__init__(master, **kwargs)
        self.master.title(title)
        self.master.columnconfigure(0, weight = 1)
        self.master.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.grid(sticky = "NEWS")
        self.create_widgets()

    def create_widgets(self):
        self.newWindow = tk.Toplevel(self.master)
        self.text = TextWindow(master = self.newWindow, title = "Text")
        self.canvas = tk.Canvas(self, bg = "cyan", width = 400, height = 400)
        self.canvas.grid(row = 0, column = 0, sticky = "NSEW")
        self.ovals = []
        self.canvas.bind("<Button-1>", self.create_oval)

    def create_oval(self, event):
        self.ovals.append(self.canvas.create_oval(event.x, event.y, event.x + 100, event.y + 50))

root = tk.Tk()
app = GraphicsWindow(master = root, title = "Graphics")
app.mainloop()
