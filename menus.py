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
        statid = 0
        while statid < 8:
            stat = randint(1, 20)
            stat = stat + 20
            try:
                attr = self.stats[statid]
            except IndexError:
                print("Index error on: " + str(statid))
            self.charstats[attr] = stat
            statid = statid + 1
        self.generatelables(self.character)

    def generatelables(self, master):
        '''This function will generate static labels for character generation menu'''
        labels = data.getstatsdesc(self.lang)
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
        for statid in range(1, 9):
            stat = statid - 1
            statval = self.stats[stat]
            statistic = " "
            if self.charstats['ws'] != None:
                statistic = self.charstats[statval]
            labl = tk.Label(master, text=statistic, bg="white",
                            fg="black", bd="10", width="10")
            if statid <= 4:
                labl.grid(row=statid, column="1", pady="5", padx="5")
            elif statid > 4 and statid < 9:
                i = statid - 4
                labl.grid(row=i, column="3", pady="5", padx="5")
            else:
                i = statid - 8
                labl.grid(row=i, column="5", pady="5", padx="5")

    def __init__(self, master, lang):
        '''This function will generate characters
        Character stats will be kept in dictionary for manipulation'''
        cleanup(master)
        self.stats = data.getstats()
        self.charstats = {}
        for stat in self.stats:
            self.charstats[stat] = None
        self.lang = lang
        self.races = data.getraces(self.lang)

        self.character = tk.Frame(master, bg="", bd="1", pady="10")
        self.character.pack()
        charlabel = data.getmenutext("char_gen_lbl", lang)
        title = tk.Label(self.character, text=charlabel)
        title.grid(row=0, column="0", columnspan="2", sticky="W")
        generatechtxt = data.getmenutext("generate_ch_txt", lang)
        generatech = tk.Button(self.character, text=generatechtxt,
                               command=self.generatestats)
        generatech.grid(row=0, column="3")
        race = ttk.Combobox(self.character, values=self.races)
        race.grid(row="1", column="6", padx="5")
        self.generatelables(self.character)

class MAINMENU:
    '''this class generates the menu'''

    def createwelcome(self, lang):
        '''This method generates initial welcome screen'''
        cleanup(self.content)
        welcome = tk.Frame(self.content, bg="red", bd="1", pady="10")
        welcome.pack()
        welcome_txt = data.getmenutext("welcome_txt", lang)
        msg = tk.Label(welcome, text=welcome_txt)
        msg.grid()

    def createmenu(self, master, lang):
        '''This function creates top level menu'''
        def character():
            '''interim function to call CHARGEN class'''
            CHARGEN(self.content, lang)
        chargen_txt = data.getmenutext('char_gen', lang)
        chargen = tk.Button(master, text=chargen_txt, command=character)
        chargen.grid(row=0, column=1)
        separator = ttk.Separator(master, orient="horizontal")
        separator.grid(row=1)

    def createquit(self, lang):
        '''This method will generate down level menu'''
        quittxt = data.getmenutext('exit_btn', lang)
        abouttxt = data.getmenutext('about_btn', lang)
        quitbtn = tk.Button(self.quitmenu, text=quittxt, command=self.quitmenu.quit)
        quitbtn.grid(row=0, column=1)
        about = tk.Button(self.quitmenu, text=abouttxt, command=infodialog)
        about.grid(row=0, column=2)

    def __init__(self, master, lang):
        mainmenu = tk.Frame(master)
        mainmenu.grid(row=1, pady=10)
        self.content = tk.Frame(master)
        self.content.grid(row=2)
        self.createmenu(mainmenu, lang)
        self.quitmenu = tk.Frame(master, pady="10")
        self.quitmenu.grid(row=3, sticky="S")
        self.createquit(lang)
        self.createwelcome(lang)

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
