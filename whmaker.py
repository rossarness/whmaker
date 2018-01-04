'''This program will generate characters for WHRP'''
import tkinter as tk
import atexit
import menus as ms
import data

class WHMAKER:
    '''This is main class for the character generator'''

    def appinit(self, master, lang="en"):
        '''Main initialization function for tk application'''
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.lang_txt = data.getmenutext('lang_txt', lang)
        self.langbtn = tk.Button(self.frame, text=self.lang_txt, command=self.regenui, height=1)
        self.langbtn.grid(row=0, column=5, padx=1, pady=2)
        ms.LANGUAGE(self.frame, lang)
        ms.MAINMENU(self.frame, lang)

    def regenui(self):
        '''This method will regenerate ui of the application'''
        ms.cleanup(self.root)
        self.appinit(self.root)

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Warhammer Character Maker")
        self.root.geometry("1280x720")
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
