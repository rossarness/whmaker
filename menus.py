'''All menus are defined as distinct classes here'''
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from random import randint
from PIL import Image, ImageTk
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
            elif statid <= 12:
                i = statid - 7
                labl.grid(row=i, column="6", pady="5", padx="5")
            elif statid <= 15:
                i = statid - 11
                labl.grid(row=i, column="8", pady="5", padx="5")
            elif statid <= 18:
                i = statid - 14
                labl.grid(row=i, column="10", pady="5", padx="5")
        birthplace = " "
        birthlbl = tk.Label(master, text=birthplace, bg="white",
                            fg="black", bd="10", width="15")
        birthlbl.grid(row=5, column=8, pady="5", padx="5",
                      columnspan=3, sticky="w")

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
        title.grid(row=0, column="0", columnspan="2", sticky="W", padx=5)
        generatechtxt = data.getmenutext("generate_ch_txt", lang)
        generatech = tk.Button(self.character, text=generatechtxt,
                               command=self.generatestats)
        generatech.grid(row=0, column="2", pady="5")
        self.raceval = tk.StringVar()
        self.raceval.trace("w", self.racechanged)
        self.raceval.set("Human")
        race = ttk.Combobox(self.character, textvariable=self.raceval,
                            values=self.races, state="readonly", width=7)
        race.grid(row="2", column="6", padx="5")
        proftxt = data.getmenutext("prof_txt", lang)
        proflabel = tk.Label(self.character, text=proftxt)
        proflabel.grid(row="0", column="3", padx=10, columnspan=2, sticky="e")
        prof = ttk.Combobox(self.character, textvariable="None", width=40)
        prof.grid(row="0", column="5", columnspan=6, pady=5, padx=5, sticky="e")
        self.generatelables(self.character)
        createseparators(self.character, 7, 1)

class MAINMENU:
    '''this class generates the menu'''

    def createwelcome(self, lang):
        '''This method generates initial welcome screen'''
        cleanup(self.content)
        welcome = tk.Frame(self.content, bd="1", pady="10")
        welcome.pack()
        welcome_txt = data.getmenutext("welcome_txt", lang)
        intro = Image.open("bg.jpg")
        introimg = ImageTk.PhotoImage(intro)
        backg = tk.Label(welcome, image=introimg)
        backg.image = introimg
        backg.grid(row=1, column=0, columnspan=6)
        msg = tk.Label(welcome, text=welcome_txt)
        msg.grid(row=0, column=0, columnspan=6)

    def createmenu(self, master, lang):
        '''This function creates top level menu'''
        def character():
            '''interim function to call CHARGEN class'''
            CHARGEN(self.content, lang)
        chargen_txt = data.getmenutext('char_gen', lang)
        inventman_txt = data.getmenutext('inv_man', lang)
        chargen = tk.Button(master, text=chargen_txt, command=character)
        invetman = tk.Button(master, text=inventman_txt, command=underdevelopment)
        invetman.grid(row=0, column=1, sticky=tk.SW)
        chargen.grid(row=0, column=0, sticky=tk.SW)

    def createquit(self, lang):
        '''This method will generate down level menu'''
        quittxt = data.getmenutext('exit_btn', lang)
        abouttxt = data.getmenutext('about_btn', lang)
        quitbtn = tk.Button(self.quitmenu, text=quittxt, command=self.quitmenu.quit)
        quitbtn.grid(row=1, column=1)
        about = tk.Button(self.quitmenu, text=abouttxt, command=infodialog)
        about.grid(row=1, column=2)

    def __init__(self, master, lang):
        mainmenu = tk.Frame(master, height=75)
        mainmenu.place(width=300, height=75, y=15, x=200)
        self.content = tk.Frame(master, height=600)
        self.content.place(width=1000, height=600, y=100, x=0)
        self.createmenu(mainmenu, lang)
        self.quitmenu = tk.Frame(master)
        self.quitmenu.place(width=150, height=50, y=650, x=450)
        self.createquit(lang)
        self.createwelcome(lang)

class LANGUAGE:
    '''This class will provide language controll for the appliation'''

    def __init__(self, master, lang):
        self.langs = data.getlanguages()
        self.langdrop = ttk.Combobox(master, value=lang,
                                     values=self.langs, state="readonly", width=15)
        name = data.getlangname(lang)
        self.langdrop.set(name)
        self.langdrop.place(width=100, height=25, y=15, x=550)

    def getlanguage(self):
        '''Return currently selected language in the combobox'''
        name = self.langdrop.get()
        lang = data.maplanguage(name)
        return lang

    def setactive(self, lang):
        '''This method sets language as activly selected'''
        data.setactive(lang)
        return lang

def infodialog():
    '''function that displays about message'''
    lang = data.getactive()
    about_btn = data.getmenutext("about_btn", lang)
    messagebox.showinfo(about_btn, "WH character maker")

def underdevelopment():
    '''function that displays function not ready message'''
    lang = data.getactive()
    warn_txt = data.getmenutext("warn", lang)
    notready = data.getmenutext("not_ready", lang)
    messagebox.showinfo(warn_txt, notready)

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
