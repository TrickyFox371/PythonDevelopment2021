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
        self.canvas.bind("<ButtonRelease-1>", self.restore_state)

    def create_oval(self, event):
        self.ovals.append(self.canvas.create_oval(event.x, event.y, event.x, event.y))
        self.cur_x = event.x
        self.cur_y = event.y
        self.canvas.bind("<Motion>", self.resize_oval)

    def resize_oval(self, event):
        x0, y0, x1, y1 =  self.canvas.coords(self.ovals[len(self.ovals) - 1])
        self.canvas.coords(self.ovals[len(self.ovals) - 1],
                           min(self.cur_x, event.x),
                           min(self.cur_y, event.y),
                           max(self.cur_x, event.x),
                           max(self.cur_y, event.y))

    def restore_state(self, event):
        self.canvas.unbind("<Motion>")

root = tk.Tk()
app = GraphicsWindow(master = root, title = "Graphics")
app.mainloop()
