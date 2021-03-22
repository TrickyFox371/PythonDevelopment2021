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
        self.canvas = tk.Canvas(self, bg = "cyan", width = 1280, height = 960)
        self.canvas.grid(row = 0, column = 0, sticky = "NSEW")
        self.ovals = []
        self.canvas.bind("<Button-1>", self.create_oval)
        self.canvas.bind("<ButtonRelease-1>", self.restore_state)

    def create_oval(self, event):
        self.ovals.append(self.canvas.create_oval(event.x, event.y, event.x, event.y))
        self.cur_x = event.x
        self.cur_y = event.y
        self.canvas.bind("<Motion>", self.resize_oval)
        self.canvas.tag_bind(self.ovals[len(self.ovals) - 1], '<Button-1>', self.start_moving)
        self.canvas.tag_bind(self.ovals[len(self.ovals) - 1], '<ButtonRelease-1>', self.restore_state)

    def resize_oval(self, event):
        x0, y0, x1, y1 = self.canvas.coords(self.ovals[len(self.ovals) - 1])
        self.canvas.coords(self.ovals[len(self.ovals) - 1],
                           min(self.cur_x, event.x),
                           min(self.cur_y, event.y),
                           max(self.cur_x, event.x),
                           max(self.cur_y, event.y))

    def start_moving(self, event):
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<ButtonRelease-1>")
        if len(self.canvas.find_withtag('current')) > 0:
            self.canvas.tag_bind(self.canvas.find_withtag('current')[0], "<Motion>", self.move_oval)

    def move_oval(self, event):
        if len(self.canvas.find_withtag('current')) > 0:
            x0, y0, x1, y1 = self.canvas.coords(self.canvas.find_withtag('current')[0])
            self.canvas.coords(self.canvas.find_withtag('current')[0],
                               event.x,
                               event.y,
                               x1 - x0 + event.x,
                               y1 - y0 + event.y)

    def restore_state(self, event):
        self.canvas.bind("<Button-1>", self.create_oval)
        self.canvas.bind("<ButtonRelease-1>", self.restore_state)
        self.canvas.unbind("<Motion>")
        if len(self.canvas.find_withtag('current')) > 0:
            self.canvas.tag_unbind(self.canvas.find_withtag('current')[0], "<Motion>")

root = tk.Tk()
app = GraphicsWindow(master = root, title = "Graphics")
app.mainloop()
