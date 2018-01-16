
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
        '''This method will generate random statistics for WFRP character'''
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
        self.racecheck()
        self.relatedskills()
        self.generate_details()
        self.generatelables(self.character)

    def generate_details(self):
        '''This function will generate all personal details for the character'''
        hair = randint(1, 10)
        self.charstats["hair"] = hair
        age = randint(1, 20)
        self.charstats['age'] = age
        eye = randint(1, 10)
        self.charstats["eye"] = eye
        weight = generateweight()
        self.charstats["weig"] = weight
        height = generate_height(self.charstats['gend'], self.charstats['race'], self.lang)
        self.charstats['heig'] = height


    def relatedskills(self):
        '''This function calculates skills which are related to other stats'''
        if self.charstats['s'] is not None:
            strength = self.charstats['s']
            strength = str(strength)
            strength = strength[0][:1]
            print(strength)

    def generatelables(self, master):
        '''This function will generate static labels for character generation menu'''
        labels = data.getstatsdesc(self.lang)
        race = self.charstats['race']
        generatelabels(master, labels)
        stats = data.getvisiblestats()
        padd = [3, 3]
        #Code below generates canvas for stats
        for statid in range(2, 19):
            stat = statid - 2
            statval = stats[stat]
            statistic = " "
            if statval == 'hair' and self.charstats['hair'] != None:
                statistic = data.gethair(self.lang, self.charstats['hair'], race)
            elif statval == 'age' and self.charstats['age'] != None:
                statistic = data.getage(self.lang, self.charstats['age'], race)
            elif statval == 'eye' and self.charstats['eye'] != None:
                statistic = data.geteye(self.lang, self.charstats['eye'], race)
            elif statval == 'weig' and self.charstats['weig'] != None:
                statistic = data.getweight(self.lang, self.charstats['weig'], race)
            elif self.charstats['ws'] != None:
                statistic = self.charstats[statval]
            labl = tk.Label(master, text=statistic, bg="white",
                            fg="black", bd="10", width="8")
            if statid <= 5:
                labl.grid(row=statid, column="1", pady=padd[0], padx=padd[1])
            elif statid <= 9:
                i = statid - 4
                labl.grid(row=i, column="3", pady=padd[0], padx=padd[1])
            elif statid <= 11:
                i = statid - 6
                labl.grid(row=i, column="6", pady=padd[0], padx=padd[1])
            elif statid <= 14:
                i = statid - 10
                labl.grid(row=i, column="8", pady=padd[0], padx=padd[1])
            elif statid <= 17:
                i = statid - 13
                labl.grid(row=i, column="10", pady=padd[0], padx=padd[1])
        birthplace = " "
        birthlbl = tk.Label(master, text=birthplace, bg="white",
                            fg="black", bd="10", width="15")
        birthlbl.grid(row=5, column=8, pady="5", padx="5",
                      columnspan=3, sticky="w")

    def racecheck(self):
        '''This method checks what race is selected and applies stat changes'''
        race = self.raceval.get()
        race_id = data.maprace(race, self.lang)
        self.charstats["race"] = race
        if self.charstats["ws"] is not None:
            if self.charstats["heig"] is None:
                self.charstats["heig"] = 0
            if race_id == "humn":
                self.charstats["heig"] = self.charstats["heig"] + 150
            elif race_id == "elvs":
                self.charstats["bs"] = self.charstats["bs"] + 10
                self.charstats["ag"] = self.charstats["ag"] + 10
                self.charstats["heig"] = self.charstats["heig"] + 160
            elif race_id == "dwrs":
                self.charstats["ws"] = self.charstats["ws"] + 10
                self.charstats["t"] = self.charstats["t"] + 10
                self.charstats["ag"] = self.charstats["ag"] - 10
                self.charstats["fel"] = self.charstats["fel"] - 10
                self.charstats["heig"] = self.charstats["heig"] + 130
            elif race_id == "hwfl":
                self.charstats["ws"] = self.charstats["ws"] - 10
                self.charstats["s"] = self.charstats["s"] - 10
                self.charstats["t"] = self.charstats["t"] - 10
                self.charstats["ag"] = self.charstats["ag"] + 10
                self.charstats["fel"] = self.charstats["fel"] + 10
                self.charstats["fel"] = self.charstats["bs"] + 10
                self.charstats["heig"] = self.charstats["heig"] + 100

    def racechanged(self, index, value, operation):
        '''This method handles race change event'''
        print("Race changed to: " + value + " index: " + index +
              " opertation: " + operation)
        old_race = self.charstats["race"]
        old_race_id = data.maprace(old_race, self.lang)
        if self.charstats["ws"] is not None:
            if old_race_id == "humn":
                self.charstats["heig"] = self.charstats["heig"] - 150
            elif old_race_id == "elvs":
                self.charstats["bs"] = self.charstats["bs"] - 10
                self.charstats["ag"] = self.charstats["ag"] - 10
                self.charstats["heig"] = self.charstats["heig"] - 160
            elif old_race_id == "dwrs":
                self.charstats["ws"] = self.charstats["ws"] - 10
                self.charstats["t"] = self.charstats["t"] - 10
                self.charstats["ag"] = self.charstats["ag"] + 10
                self.charstats["fel"] = self.charstats["fel"] + 10
                self.charstats["heig"] = self.charstats["heig"] - 130
            elif old_race_id == "hwfl":
                self.charstats["ws"] = self.charstats["ws"] + 10
                self.charstats["s"] = self.charstats["s"] + 10
                self.charstats["t"] = self.charstats["t"] + 10
                self.charstats["ag"] = self.charstats["ag"] - 10
                self.charstats["fel"] = self.charstats["fel"] - 10
                self.charstats["fel"] = self.charstats["bs"] - 10
                self.charstats["heig"] = self.charstats["heig"] - 100
        self.racecheck()
        self.relatedskills()
        self.generatelables(self.character)

    def genderchanged(self, index, value, operation):
        '''This method handles gender change event'''
        print("Gender changed to: " + value + " index: " + index +
              " opertation: " + operation)
        if self.charstats['gend'] is not None:
            old_gender = self.charstats['gend']
            old_gender_id = data.mapmenutext(old_gender, self.lang)
        new_gender = self.gendervalue.get()
        self.charstats['gend'] = new_gender
        if self.charstats['heig'] is not None:
            race = self.charstats['race']
            race_id = data.maprace(race, self.lang)
            if old_gender_id == "male":
                if race_id == 'dwrs':
                    height = self.charstats['heig'] - 15
                    self.charstats['heig'] = height
                else:
                    height = self.charstats['heig'] - 10
                    self.charstats['heig'] = height
            elif old_gender_id == "female":
                if race_id == 'dwrs':
                    height = self.charstats['heig'] + 15
                    self.charstats['heig'] = height
                else:
                    height = self.charstats['heig'] + 10
                    self.charstats['heig'] = height
        self.generatelables(self.character)

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
        label = data.getmenutext("char_gen_lbl", lang)
        title = tk.Label(self.character, text=label)
        title.grid(row=0, column="0", columnspan="2", sticky="W", padx=5)
        label = data.getmenutext("generate_ch_txt", lang)
        generatech = tk.Button(self.character, text=label,
                               command=self.generatestats)
        generatech.grid(row=0, column="2", pady="5")
        self.raceval = tk.StringVar()
        self.raceval.trace("w", self.racechanged)
        defaultrace = data.getrace("humn", self.lang)
        self.charstats["race"] = defaultrace
        self.raceval.set(defaultrace)
        race = ttk.Combobox(self.character, textvariable=self.raceval,
                            values=self.races, state="readonly", width=7)
        race.grid(row="2", column="6", padx="5")
        self.gendervalue = tk.StringVar()
        self.gendervalue.trace("w", self.genderchanged)
        genders = data.getgenders(self.lang)
        gender = ttk.Combobox(self.character, values=genders, state="readonly",
                              textvariable=self.gendervalue, width=7)
        gender.grid(row="3", column="6", padx="5")
        default_gender = data.getmenutext("male", self.lang)
        self.gendervalue.set(default_gender)
        label = data.getmenutext("prof_txt", lang)
        proflabel = tk.Label(self.character, text=label)
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
    '''This class will provide language controll for the application'''

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
        name = data.getlangname(lang)
        self.langdrop.set(name)
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
        elif pos > 4 and col == 9:
            pos = 8
            col = 2
        else:
            pos = pos + 1

def generateweight():
    '''Function that will generate weight and return id to the character stats
    Due to complex algorithm separate function is required'''
    initial = randint(1, 100)
    if initial == 1:
        weight_id = 1
    elif initial <= 10:
        weight_id = 2
    elif initial <= 20:
        weight_id = 3
    elif initial <= 30:
        weight_id = 4
    elif initial <= 40:
        weight_id = 5
    elif initial <= 50:
        weight_id = 6
    elif initial <= 60:
        weight_id = 7
    elif initial <= 70:
        weight_id = 8
    elif initial <= 80:
        weight_id = 9
    elif initial <= 90:
        weight_id = 10
    elif initial <= 99:
        weight_id = 11
    elif initial == 100:
        weight_id = 12
    return weight_id

def generate_height(gender, race, lang):
    '''Generates height of the character based on gender and race'''
    print("DEBUG: gender value is: " + gender)
    genderid = data.mapmenutext(gender, lang)
    raceid = data.maprace(race, lang)
    roll1 = randint(1, 10)
    roll2 = randint(1, 10)
    totalroll = roll1 + roll2
    if genderid == "female":
        if raceid == "humn":
            height = 150 + totalroll
        elif raceid == "elvs":
            height = 160 + totalroll
        elif raceid == "dwrs":
            height = 130 + totalroll
        elif raceid == "hwfl":
            height = 100 + totalroll
    elif genderid == "male":
        if raceid == "humn":
            height = 160 + totalroll
        elif raceid == "elvs":
            height = 170 + totalroll
        elif raceid == "dwrs":
            height = 145 + totalroll
        elif raceid == "hwfl":
            height = 110 + totalroll
    return height

def generate_mark():
    '''This function will generate distinguishing mark for the character'''
    roll = randint(1, 100)
    if roll < 6:
        mark_id = 1
    elif roll < 11:
        mark_id = 2
    elif roll < 16:
        mark_id = 3
    elif roll < 21:
        mark_id = 4
    elif roll < 26:
        mark_id = 5
    elif roll < 30:
        mark_id = 6
    elif roll < 36:
        mark_id = 7
    elif roll < 40:
        mark_id = 8
    elif roll < 46:
        mark_id = 9
    elif roll < 51:
        mark_id = 10
    elif roll < 56:
        mark_id = 11
    elif roll < 61:
        mark_id = 12
    elif roll < 66:
        mark_id = 13
    elif roll < 71:
        mark_id = 14
    elif roll < 76:
        mark_id = 15
    elif roll < 81:
        mark_id = 16
    elif roll < 85:
        mark_id = 17
    elif roll < 90:
        mark_id = 18
    elif roll < 95:
        mark_id = 19
    elif roll < 99:
        mark_id = 20
    else:
        mark_id = 21
    return mark_id
