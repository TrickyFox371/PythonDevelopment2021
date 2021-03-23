import tkinter as tk
import inspect

class GraphicsWindow(tk.Frame):
    def __init__(self, master = None, title = "<application>", **kwargs):
        super().__init__(master, **kwargs)
        self.master.title(title)
        self.master.columnconfigure(0, weight = 1)
        self.master.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.grid(sticky = "NEWS")
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, bg = "cyan", width = 800, height = 600)
        self.canvas.grid(row = 0, column = 0, sticky = "NSEW")
        self.ovals = []
        self.canvas.bind("<Button-1>", self.create_oval)
        self.canvas.bind("<ButtonRelease-1>", self.restore_state)

        self.text = tk.Text()
        self.text.grid(row = 0, column = 1, sticky = "NSEW")

    def create_oval(self, event):
        self.ovals.append((self.canvas.create_oval(event.x, event.y,
                                                  event.x, event.y,
                                                  fill = "green",
                                                  outline = "black"),
                           "green", "black"))
        self.cur_x = event.x
        self.cur_y = event.y
        self.canvas.bind("<Motion>", self.resize_oval)
        self.canvas.tag_bind(self.ovals[len(self.ovals) - 1][0], '<Button-1>', self.start_moving)
        self.canvas.tag_bind(self.ovals[len(self.ovals) - 1][0], '<ButtonRelease-1>', self.restore_state)

    def resize_oval(self, event):
        x0, y0, x1, y1 = self.canvas.coords(self.ovals[len(self.ovals) - 1][0])
        self.canvas.coords(self.ovals[len(self.ovals) - 1][0],
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
        self.refresh_text()

    def refresh_text(self):
        self.text.delete('1.0', tk.END)
        i = 1
        for oval in self.ovals:
            x0, y0, x1, y1 = self.canvas.coords(oval[0])
            self.text.insert(str(i) + ".0", "oval <" + str(x0) + " " + str(y0) + " " +
                                                       str(x1) + " " + str(y1) + "> " +
                                                       oval[1] + " " + oval[2] + "\n")
            i = i + 1
            

root = tk.Tk()
app = GraphicsWindow(master = root, title = "Graphics")
app.mainloop()
