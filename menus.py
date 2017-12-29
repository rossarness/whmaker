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
        self.content = tk.Frame(master, width=700, height=400, bg="", bd="1", pady="10")
        self.content.pack()

class WELCOME:
    '''This is initial welcome screen class'''
    def __init__(self, master):
        self.welcome = tk.Frame(master, width=700, height=700, bg="red", bd="1", pady="10")
        self.welcome.pack()
        self.msg = tk.Label(self.welcome, text="Welcome to WHRP character generation application")
        self.msg.grid()
