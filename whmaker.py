'''This program will generate characters for WHRP'''
import tkinter as tk
from tkinter import messagebox
import atexit
import menus as ms
import data


class WHMAKER:
    '''This is main class for the character generator'''

    def createmenu(self, master, lang):
        '''This function creates top level menu'''
        def character():
            '''interim function to call CHARGEN class'''
            ms.CHARGEN(self.content, lang)
        chargen_txt = data.getmenutext('char_gen', lang)
        self.chargen = tk.Button(master, text=chargen_txt, command=character)
        self.chargen.grid(row=0, column=1)

    def createquit(self, master, lang):
        '''This method will generate down level menu'''
        self.quittxt = data.getmenutext('exit_btn', lang)
        self.abouttxt = data.getmenutext('about_btn', lang)
        self.quit = tk.Button(master, text=self.quittxt, command=self.frame.quit)
        self.quit.grid(row=0, column=1)
        self.about = tk.Button(master, text=self.abouttxt, command=infodialog)
        self.about.grid(row=0, column=2)

    def __init__(self, master, lang):
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.mainmenu = tk.Frame(self.frame)
        self.mainmenu.grid(row=1, pady=10)
        self.content = tk.Frame(self.frame)
        self.content.grid(row=2)
        self.createmenu(self.mainmenu, lang)
        ms.WELCOME(self.content, lang)

        self.quitmenu = tk.Frame(self.frame, pady="10")
        self.quitmenu.grid(row=3)
        self.createquit(self.quitmenu, lang)

def main():
    '''Main function'''
    lang = "en"
    root = tk.Tk()
    root.title("Warhammer Character Maker")
    root.geometry("1280x720")
    atexit.register(exit_handler)
    app = WHMAKER(root, lang)
    maintitle = tk.Label(app.frame, text="Warhammer Character Maker")
    maintitle.grid(row=0)
    root.mainloop()

def infodialog():
    '''function that displays about message'''
    messagebox.showinfo("About", "WH character maker")

def exit_handler():
    '''App exit handler'''
    data.closedb()

if __name__ == "__main__":
    main()
