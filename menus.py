'''All menus are defined as distinct classes here'''
import tkinter as tk
from random import randint
import data

def cleanup(widget):
    '''Widget cleanup function'''
    for child in widget.winfo_children():
        child.destroy()

class CHARGEN:
    '''This is character generation class'''
    def generatestats(self, master):
        '''This method will generate random statistics for WHFRP character'''
        for stats in range(1, 9):
            stat = randint(1, 20)
            stat = stat + 20
            self.labl = tk.Label(master, text=stat, bg="white",
                                 fg="black", bd="10", width="10")
            if stats <= 4:
                self.labl.grid(row=stats, column="0", pady="5", padx="5")
            else:
                i = stats - 4
                self.labl.grid(row=i, column="2", pady="5", padx="5")

    def __init__(self, master, lang):
        '''This function will generate character menu'''
        cleanup(master)
        self.character = tk.Frame(master, bg="", bd="1", pady="10")
        self.character.pack()
        self.charlabel = data.getmenutext("char_gen_lbl", lang)
        self.title = tk.Label(self.character, text=self.charlabel)
        self.title.grid(row=0, column="0")
        self.generatestats(self.character)

class WELCOME:
    '''This is initial welcome screen class'''
    def __init__(self, master, lang):
        self.welcome = tk.Frame(master, bg="red", bd="1", pady="10")
        self.welcome.pack()
        self.welcome_txt = data.getmenutext("welcome_txt", lang)
        self.msg = tk.Label(self.welcome, text=self.welcome_txt)
        self.msg.grid()
