import tkinter as tk
from tkinter.messagebox import *

def parseGeom(geom):
    row = 0
    weight = 1
    rowspan = 0
    column = 0
    weightCol = 1
    columnspan = 0
    sticky = "NEWS"
    tmp = 0
    tmp2 = ""
    state = "0"
    for sym in geom:
        if sym.isdigit():
            tmp = tmp * 10
            tmp = tmp + int(sym)
        elif sym.isalpha():
            tmp2 = tmp2 + sym
        else:
            if state == "0":
                row = tmp
                tmp = 0
                if (sym == "."):
                    state = "1"
                elif (sym == "+"):
                    state = "2"
                elif (sym == ":"):
                    state = "3"
            elif state == "1":
                weight = tmp
                tmp = 0
                if (sym == "+"):
                    state = "2"
                elif (sym == ":"):
                    state = "3"
            elif state == "2":
                rowspan = tmp
                tmp = 0
                state = "3"
            if state == "3":
                column = tmp
                tmp = 0
                if (sym == "."):
                    state = "4"
                elif (sym == "+"):
                    state = "5"
                elif (sym == "/"):
                    state = "6"
            elif state == "4":
                weightCol = tmp
                tmp = 0
                if (sym == "+"):
                    state = "5"
                elif (sym == "/"):
                    state = "6"
            elif state == "5":
                columnspan = tmp
                tmp = 0
                state = "6"
            elif state == "6":
                sticky = tmp2
    if state == "0":
        row = tmp
    elif state == "1":
        weight = tmp
    elif state == "2":
        rowspan = tmp
    elif state == "3":
        column = tmp
    elif state == "4":
        weightCol = tmp
    elif state == "5":
        columnspan = tmp
    elif state == "6":
       sticky = tmp2
    return (row, weight, rowspan + 1, column, weightCol, columnspan + 1, sticky)

class Application(tk.Frame):

    def __init__(self, master=None, title="<application>", **kwargs):
        '''Create root window with frame, tune weight and resize'''
        super().__init__(master, **kwargs)
        self.master.title(title)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        self.createWidgets()

    def __getattr__(self, obj):
        if obj in dir(self):
            return self[obj]
        self.widgetName = obj
        return self.addWidget

    def addWidget(self, obj, geom, **kwargs):

        class decorClass(obj):
            def __getattr__(self, obj):
                if obj in dir(self):
                    return self[obj]
                self.widgetName = obj
                return self.addWidget
            def addWidget(self, obj, geom, **kwargs):
                instance = obj(master = self, **kwargs)
                setattr(self, self.widgetName, instance)
                results = parseGeom(geom)
                self.rowconfigure(results[0], weight = results[1])
                self.columnconfigure(results[3], weight = results[4])
                instance.grid(row = results[0],
                              column = results[3],
                              rowspan = results[2],
                              columnspan = results[5],
                              sticky = results[6])
                

        instance = decorClass(master = self, **kwargs)
        setattr(self, self.widgetName, instance)
        results = parseGeom(geom)
        self.rowconfigure(results[0], weight = results[1])
        self.columnconfigure(results[3], weight = results[4])
        instance.grid(row = results[0],
                      column = results[3],
                      rowspan = results[2],
                      columnspan = results[5],
                      sticky = results[6])
        

    def createWidgets(self):
       pass

class App(Application):
    def createWidgets(self):
        self.message = "Congratulations!\nYou've found a sercet level!"
        self.F1(tk.LabelFrame, "1:0", text="Frame 1")
        self.F1.B1(tk.Button, "0:0/NW", text="1")
        self.F1.B2(tk.Button, "0:1/NE", text="2")
        self.F1.B3(tk.Button, "1:0+1/SEW", text="3")
        self.F2(tk.LabelFrame, "1:1", text="Frame 2")
        self.F2.B1(tk.Button, "0:0/N", text="4")
        self.F2.B2(tk.Button, "0+1:1/SEN", text="5")
        self.F2.B3(tk.Button, "1:0/S", text="6")
        self.Q(tk.Button, "2.0:1.2/SE", text="Quit", command=self.quit)
        self.F1.B3.bind("<Any-Key>", lambda event: showinfo(self.message.split()[0], self.message))

app = App(title="Sample application")
app.mainloop()
