'''This program will generate characters for WHRP'''
import tkinter as tk
import atexit
import menus as ms
import data

class WHMAKER:
    '''This is main class for the character generator'''

    def appinit(self, master, lang="en"):
        '''Main initialization function for tk application'''
        frame = tk.Frame(master)
        frame.pack()
        lang_txt = data.getmenutext('lang_txt', lang)
        langbtn = tk.Button(frame, text=lang_txt, command=self.regenui, height=1)
        langbtn.grid(row=0, column=5, padx=1, pady=2)
        self.language = ms.LANGUAGE(frame, lang)
        self.menu = ms.MAINMENU(frame, lang)

    def regenui(self):
        '''This method will regenerate ui of the application'''
        lang = self.language.getlanguage()
        ms.cleanup(self.root)
        self.appinit(self.root, lang)

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Warhammer Character Maker")
        self.root.geometry("1000x500")
        self.appinit(self.root)
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
