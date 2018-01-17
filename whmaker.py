'''This program will generate characters for WHRP'''
import tkinter as tk
import atexit
import menus as ms
import data

class WHMAKER:
    '''This is main class for the character generator'''

    def appinit(self, master, lang="en"):
        '''Main initialization function for tk application'''
        lang_txt = data.getmenutext('lang_txt', lang)
        langbtn = tk.Button(master, text=lang_txt, command=self.regenui)
        langbtn.place(width=125, height=25, y=15, x=660)
        self.language = ms.LANGUAGE(master, lang)
        self.menu = ms.MAINMENU(master, lang)

    def regenui(self):
        '''This method will regenerate ui of the application'''
        lang = self.language.getlanguage()
        self.language.setactive(lang)
        ms.cleanup(self.root)
        self.appinit(self.root, lang)

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Warhammer Character Maker")
        self.root.geometry("1000x700")
        self.root.resizable(0, 0)
        lang = data.getactive()
        self.appinit(self.root, lang)
        self.root.mainloop()

def main():
    '''Main function'''
    atexit.register(exit_handler)
    WHMAKER()

def exit_handler():
    '''App exit handler'''
    data.closedb()

if __name__ == "__main__":
    main()
