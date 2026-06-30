from tkinter import *

root = Tk()
root.title("Form")
root.geometry("600x600")
root.resizable(False, False)

def submit_form():
    name = nameVal.get()
    email = emailVal.get()
    password = passwordVal.get()
    confirm_password = confirmPasswordVal.get()
    agree_terms = checkVar.get()

    if not name or not email or not password or not confirm_password:
        print("Please fill in all fields.")
        return

    if password != confirm_password:
        print("Passwords do not match.")
        return

    if not agree_terms:
        print("You must agree to the terms and conditions.")
        return

    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Password: {password}")
    print("Form submitted successfully!")

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

checkVar = IntVar()
checkButton = Checkbutton(root, text="I agree to the terms and conditions", variable=checkVar).place(x=200, y=260)

Button(root, text="Submit", width=20, height=2, bg="blue", fg="white", command=submit_form).place(x=200, y=300)
root.mainloop()