'''All menus are defined as distinct classes here'''
import tkinter as tk

def cleanup(widget):
    '''Widget cleanup function'''
    for child in widget.winfo_children():
        child.destroy()

class CHARGEN:
    '''This is character generation class'''
    def __init__(self, master):
        '''This function will generate character menu'''
        cleanup(master)
        self.character = tk.Frame(master, bg="", bd="1", pady="10")
        self.character.pack()
        self.title = tk.Label(self.character, text="Character generation menu")
        self.title.grid(row=0)
        stats = 8
        while stats <= 8:
            

class WELCOME:
    '''This is initial welcome screen class'''
    def __init__(self, master):
        self.welcome = tk.Frame(master, bg="red", bd="1", pady="10")
        self.welcome.pack()
        self.msg = tk.Label(self.welcome, text="Welcome to WHRP character generation application")
        self.msg.grid()
