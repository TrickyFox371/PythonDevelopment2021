import tkinter as tk
import re

COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99',
    'white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']

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
        self.text.bind("<KeyRelease>", self.check_text)

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

    def check_text(self, event):
        for tag in self.text.tag_names():
            self.text.tag_delete(tag)
        strings = self.text.get("1.0", tk.END).split("\n")
        i = 0
        all_is_fine = True
        wordlist = []
        for string in strings:
            if string == "":
                i = i + 1
                continue
            words = string.split(" ")
            while " " in words:
                words.remove(" ")
            while "" in words:
                words.remove("")
            if len(words) != 7:
                self.text.tag_add(str(i), str(i + 1) + ".0", str(i + 1) + "." + str(len(string)))
                self.text.tag_config(str(i), background = "red")
                all_is_fine = False
                i = i + 1
                continue
            if words[0] != "oval":
                self.text.tag_add(str(i), str(i + 1) + ".0", str(i + 1) + "." + str(len(string)))
                self.text.tag_config(str(i), background = "red")
                all_is_fine = False
                i = i + 1
                continue
            if (not words[1].replace('.', '', 1).lstrip('-').isdigit()) or \
               (not words[2].replace('.', '', 1).lstrip('-').isdigit()) or \
               (not words[3].replace('.', '', 1).lstrip('-').isdigit()) or \
               (not words[4].replace('.', '', 1).lstrip('-').isdigit()):
                self.text.tag_add(str(i), str(i + 1) + ".0", str(i + 1) + "." + str(len(string)))
                self.text.tag_config(str(i), background = "red")
                all_is_fine = False
                i = i + 1
                continue
            if (words[5][0] != "(" or words[5][-1] != ")" or words[6][0] != "(" or words[6][-1] != ")"):
                self.text.tag_add(str(i), str(i + 1) + ".0", str(i + 1) + "." + str(len(string)))
                self.text.tag_config(str(i), background = "red")
                all_is_fine = False
                i = i + 1
                continue
            else:
                words[5] = words[5][1:-1]
                words[6] = words[6][1:-1]
            if (not (words[5].replace("_", " ") in COLORS or re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', words[5]))) or \
               (not (words[6].replace("_", " ") in COLORS or re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', words[6]))):
                self.text.tag_add(str(i), str(i + 1) + ".0", str(i + 1) + "." + str(len(string)))
                self.text.tag_config(str(i), background = "red")
                all_is_fine = False
                i = i + 1
                continue
            i = i + 1
            wordlist.append(words)
        if all_is_fine:
            self.canvas.delete("all")
            self.ovals = []
            for words in wordlist:
                self.ovals.append((self.canvas.create_oval(float(words[1]), float(words[2]),
                                                           float(words[3]), float(words[4]),
                                                           fill = words[5].replace("_", " "),
                                                           outline = words[6].replace("_", " ")),
                                   words[5], words[6]))
                self.canvas.tag_bind(self.ovals[len(self.ovals) - 1][0], '<Button-1>', self.start_moving)
                self.canvas.tag_bind(self.ovals[len(self.ovals) - 1][0], '<ButtonRelease-1>', self.restore_state)

    def refresh_text(self):
        self.text.delete("1.0", tk.END)
        i = 1
        for oval in self.ovals:
            x0, y0, x1, y1 = self.canvas.coords(oval[0])
            self.text.insert(str(i) + ".0", "oval " + str(x0) + " " + str(y0) + " " +
                                                      str(x1) + " " + str(y1) + " (" +
                                                      oval[1] + ") (" + oval[2] + ")\n")
            i = i + 1
            

root = tk.Tk()
app = GraphicsWindow(master = root, title = "Graphics")
app.mainloop()
