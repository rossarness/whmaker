'''This program will generate characters for WHRP'''
import tkinter as tk
from tkinter import messagebox
import menus as ms

class WHMAKER:
    '''This is main class for the character generator'''

    def createmenu(self, master):
        '''This function creates top level menu'''
        def character():
            '''interim function to call CHARGEN class'''
            ms.CHARGEN(self.content)
        self.chargen = tk.Button(master, text="Character Creation",
                                 command=character)
        self.chargen.grid(row=0, column=1)

    def createquit(self, master):
        '''This method will generate down level menu'''
        self.quit = tk.Button(master, text="Quit", command=self.frame.quit)
        self.quit.grid(row=0, column=1)
        self.about = tk.Button(master, text="About", command=infodialog)
        self.about.grid(row=0, column=2)

    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.mainmenu = tk.Frame(self.frame)
        self.mainmenu.grid(row=1, pady=10)
        self.content = tk.Frame(self.frame)
        self.content.grid(row=2)
        self.createmenu(self.mainmenu)
        ms.WELCOME(self.content)

        self.quitmenu = tk.Frame(self.frame, pady="10")
        self.quitmenu.grid(row=3)
        self.createquit(self.quitmenu)

def main():
    '''Main function'''
    root = tk.Tk()
    root.title("Warhammer Character Maker")
    root.geometry("1280x720")

    app = WHMAKER(root)
    maintitle = tk.Label(app.frame, text="Warhammer Character Maker")
    maintitle.grid(row=0)
    root.mainloop()

def infodialog():
    '''function that displays about message'''
    messagebox.showinfo("About", "WH character maker")

if __name__ == "__main__":
    main()
