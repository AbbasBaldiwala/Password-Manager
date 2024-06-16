from tkinter import *
import passwordGenerator

IMG_WIDTH = 200
IMG_HEIGHT = 200
FONT_NAME = "Courier"
BG = "black"
PADDING = 20

window = Tk()
window.config(padx=PADDING, pady=PADDING)
canvas = Canvas(width=IMG_WIDTH, height=IMG_HEIGHT, highlightthickness=0)

bgImage = PhotoImage(file="logo.png")
canvas.create_image(IMG_WIDTH / 2, IMG_HEIGHT / 2, image=bgImage)
canvas.grid(column=1, row=0)

def addInfo():
    website = websiteEntry.get()
    email = emailEntry.get()
    password = passEntry.get()
    info: str = f"{website} | {email} | {password}\n"
    with open(file="Login_Info.txt", mode="a") as outputFile:
        outputFile.writelines(info)

def generatePassword():
    passEntry.delete(0,END)
    password = passwordGenerator.generateRandomPassword()
    passEntry.insert(END, string=password)


websiteLabel = Label(text="Website:", font=(FONT_NAME, 12, "normal"))
websiteLabel.grid(column=0, row=1)

emailLabel = Label(text="Email/Username:", font=(FONT_NAME, 12, "normal"))
emailLabel.grid(column=0, row=2)

passLabel = Label(text="Password:", font=(FONT_NAME, 12, "normal"))
passLabel.grid(column=0, row=3)

websiteEntry = Entry(width=40, highlightthickness=0)
websiteEntry.grid(column=1, row=1, columnspan=2)

emailEntry = Entry(width=40, highlightthickness=0)
emailEntry.grid(column=1, row=2, columnspan=2)


passEntry = Entry(width=21, highlightthickness=0)
passEntry.grid(column=1, row=3)


genPass = Button(text="Generate Password", bg="gray", width=15, command=generatePassword)
genPass.grid(column=2, row=3)

addButton = Button(text="Add", width=37, command=addInfo)
addButton.grid(column=1, row=4, columnspan=2)




window.mainloop()
