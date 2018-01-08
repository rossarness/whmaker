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
        generatelabels(master, labels)
        #Code below generates canvas for stats
        for statid in range(2, 20):
            stat = statid - 2
            statval = self.stats[stat]
            statistic = " "
            if self.charstats['ws'] != None:
                statistic = self.charstats[statval]
            labl = tk.Label(master, text=statistic, bg="white",
                            fg="black", bd="10", width="5")
            if statid <= 5:
                labl.grid(row=statid, column="1", pady="5", padx="5")
            elif statid <= 9:
                i = statid - 4
                labl.grid(row=i, column="3", pady="5", padx="5")
            elif statid <= 11:
                i = statid - 6
                labl.grid(row=i, column="6", pady="5", padx="5")
            elif statid <= 15:
                i = statid - 10
                labl.grid(row=i, column="8", pady="5", padx="5")
            elif statid <= 19:
                i = statid - 14
                labl.grid(row=i, column="10", pady="5", padx="5")

    def racechanged(self, index, value, operation):
        '''This method handles race change event'''
        print("Race changed to: " + value + " index: " + index +
              " opertation: " + operation)
        print("Value in box is: " + self.raceval.get())
        print("Value in the variable is: " + str(self.raceval))


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
        generatech.grid(row=0, column="3", pady="5")
        self.raceval = tk.StringVar()
        self.raceval.trace("w", self.racechanged)
        self.raceval.set("Human")
        race = ttk.Combobox(self.character, textvariable=self.raceval,
                            values=self.races, state="readonly", width=7)
        race.grid(row="2", column="6", padx="5")
        prof = ttk.Combobox(self.character, textvariable="None", width=7)
        prof.grid(row="3", column="6", pady=5, padx=5)
        self.generatelables(self.character)
        createseparators(self.character, 7, 1)

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
        inventman_txt = data.getmenutext('inv_man', lang)
        chargen = tk.Button(master, text=chargen_txt, command=character)
        invetman = tk.Button(master, text=inventman_txt, command=underdevelopment)
        invetman.grid(row=0, column=1, sticky="sw")
        chargen.grid(row=0, column=0, sticky="sw")

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
        mainmenu.grid(row=0, pady=10)
        self.content = tk.Frame(master)
        self.content.grid(row=1)
        self.createmenu(mainmenu, lang)
        self.quitmenu = tk.Frame(master, pady="10")
        self.quitmenu.grid(row=2, sticky="sw")
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
        self.langdrop.grid(row=0, column=4, padx=2, pady=2)

    def getlanguage(self):
        '''Return currently selected language in the combobox'''
        name = self.langdrop.get()
        lang = data.maplanguage(name)
        return lang

    def setactive(self, lang):
        '''This method sets language as activly selected'''
        return lang

def infodialog():
    '''function that displays about message'''
    messagebox.showinfo("About", "WH character maker")

def underdevelopment():
    '''function that displays function not ready message'''
    messagebox.showinfo("Warning!", "This function is not ready yet.")

def createseparators(master, row1, row2):
    '''This method generates separators for UI'''
    sep2 = ttk.Separator(master)
    sep1 = ttk.Separator(master)
    sep1.grid(row=row1, sticky="ew", columnspan=15)
    sep2.grid(row=row2, sticky="ew", columnspan=15)

def generatelabels(master, labels):
    '''This function will generates labels for character menu'''
    pos = 2
    col = 0
    for label in labels:
        labl = tk.Label(master, text=label)
        labl.grid(row=pos, column=col, pady="5", padx="5")
        if pos > 4 and col == 0:
            pos = 2
            col = 2
        elif pos > 4 and col == 2:
            pos = 2
            col = 4
        elif pos > 4 and col == 4:
            pos = 2
            col = 7
        elif pos > 4 and col == 7:
            pos = 2
            col = 9
        else:
            pos = pos + 1
