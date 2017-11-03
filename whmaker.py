import tkinter as tk

class whmaker:

  def about(self):
    print("Warhammer Character Maker")

  def __init__(self, master):
    self.frame = tk.Frame(master)
    self.frame.pack()
  
    self.Label = tk.Label(self.frame, text="Warhammer Character Maker")
    self.Label.pack()

    self.quit = tk.Button(self.frame, text="Quit", command=self.frame.quit)
    self.quit.pack( side = tk.BOTTOM )
    self.about = tk.Button(self.frame, text="About", command=self.about)
    self.about.pack( side = tk.BOTTOM)

def main():
  root = tk.Tk()
  root.title("Warhammer Character Maker")
  root.geometry("1280x720")

  app = whmaker(root)
  content = tk.Label(app.frame, text="This is the content")
  content.pack( side = tk.TOP)
  root.mainloop()

if __name__ == "__main__":
  main()