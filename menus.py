'''All menus are defined as distinct classes here'''
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from random import randint
import data

def cleanup(widget):
    '''Widget cleanup function'''
    for child in widget.winfo_children():
        child.destroy()

class CHARGEN:
    '''This is character generation class'''
    def generatestats(self):
        '''This method will generate random statistics for WHFRP character'''
        stats = 0
        self.charstats = []
        while stats < 9:
            stat = randint(1, 20)
            stat = stat + 20
            self.charstats.append(stat)
            stats = stats + 1
        self.generatelables(self.character, self.lang)

    def generatelables(self, master, lang):
        '''This function will generate static labels for character generation menu'''
        labels = data.getstatsdesc(lang)
        pos = 1
        col = 0
        for label in labels:
            labl = tk.Label(master, text=label)
            labl.grid(row=pos, column=col, pady="5", padx="5")
            if pos > 3:
                pos = 1
                col = 2
            else:
                pos = pos + 1
        for stats in range(1, 9):
            stat = stats - 1
            statistic = " "
            if self.charstats[0] != None:
                statistic = self.charstats[stat]
            labl = tk.Label(master, text=statistic, bg="white",
                            fg="black", bd="10", width="10")
            if stats <= 4:
                labl.grid(row=stats, column="1", pady="5", padx="5")
            else:
                i = stats - 4
                labl.grid(row=i, column="3", pady="5", padx="5")

    def __init__(self, master, lang):
        '''This function will generate character menu'''
        cleanup(master)
        self.lang = lang
        self.charstats = []
        self.charstats.append(None)
        self.character = tk.Frame(master, bg="", bd="1", pady="10")
        self.character.pack()
        self.charlabel = data.getmenutext("char_gen_lbl", lang)
        self.title = tk.Label(self.character, text=self.charlabel)
        self.title.grid(row=0, column="0", columnspan="2", sticky="W")
        self.generatechtxt = data.getmenutext("generate_ch_txt", lang)
        self.generatech = tk.Button(self.character, text=self.generatechtxt,
                                    command=self.generatestats)
        self.generatech.grid(row=0, column="3")
        self.generatelables(self.character, lang)

class WELCOME:
    '''This is initial welcome screen class'''
    def __init__(self, master, lang):
        cleanup(master)
        self.welcome = tk.Frame(master, bg="red", bd="1", pady="10")
        self.welcome.pack()
        self.welcome_txt = data.getmenutext("welcome_txt", lang)
        self.msg = tk.Label(self.welcome, text=self.welcome_txt)
        self.msg.grid()

class MAINMENU:
    '''this class generates the menu'''

    def createmenu(self, master, lang):
        '''This function creates top level menu'''
        def character():
            '''interim function to call CHARGEN class'''
            CHARGEN(self.content, lang)
        chargen_txt = data.getmenutext('char_gen', lang)
        chargen = tk.Button(master, text=chargen_txt, command=character)
        chargen.grid(row=0, column=1)

    def createquit(self, master, lang):
        '''This method will generate down level menu'''
        quittxt = data.getmenutext('exit_btn', lang)
        abouttxt = data.getmenutext('about_btn', lang)
        quitbtn = tk.Button(master, text=quittxt, command=master.quit)
        quitbtn.grid(row=0, column=1)
        self.about = tk.Button(master, text=abouttxt, command=infodialog)
        self.about.grid(row=0, column=2)

    def __init__(self, master, lang):
        self.mainmenu = tk.Frame(master)
        self.mainmenu.grid(row=1, pady=10)
        self.content = tk.Frame(master)
        self.content.grid(row=2)
        self.createmenu(self.mainmenu, lang)
        quitmenu = tk.Frame(master, pady="10")
        quitmenu.grid(row=3, sticky="S")
        self.createquit(quitmenu, lang)
        WELCOME(self.content, lang)

class LANGUAGE:
    '''This class will provide language controll for the appliation'''

    def __init__(self, master, lang):
        self.langs = data.getlanguages()
        self.langdrop = ttk.Combobox(master, value=lang,
                                     values=self.langs, state="readonly", width=10)
        name = data.getlangname(lang)
        self.langdrop.set(name)
        self.langdrop.grid(row=0, column="4", padx=2, pady=2)

    def getlanguage(self):
        '''Return currently selected language in the combobox'''
        name = self.langdrop.get()
        lang = data.maplanguage(name)
        return lang


def infodialog():
    '''function that displays about message'''
    messagebox.showinfo("About", "WH character maker")
