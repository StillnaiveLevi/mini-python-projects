from tkinter import *

root = Tk()
root.title("Form")
root.geometry("600x600")
root.resizable(False, False)

Label(root, text="Name", font = "Arial 12").place(x=50, y=50)

root.mainloop()