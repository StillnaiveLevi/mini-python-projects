from tkinter import *

root = Tk()
root.title("Form")
root.geometry("600x600")
root.resizable(False, False)

Label(root, text="SignUp", font = "Arial 12").place(x=50, y=50)

Label(root, text = "Full Name", font = "Arial 10").place(x=50, y=100)
Label(root, text = "Email", font = "Arial 10").place(x=50, y=140)
Label(root, text = "Password", font = "Arial 10").place(x=50, y=180)
Label(root, text = "Confirm Password", font = "Arial 10").place(x=50, y=220)

nameVal = StringVar()
emailVal = StringVar()
passwordVal = StringVar()
confirmPasswordVal = StringVar()

nameEntry = Entry(root, textvariable=nameVal, width=30).place(x=200, y=100)
emailEntry = Entry(root, textvariable=emailVal, width=30).place(x=200
, y=140)
passwordEntry = Entry(root, textvariable=passwordVal, width=30).place(x=200, y=180)
confirmPasswordEntry = Entry(root, textvariable=confirmPasswordVal, width=30).place(x=200, y=220)
root.mainloop()