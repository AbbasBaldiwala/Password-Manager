from tkinter import *
from tkinter import messagebox
import json
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

def search():
    website = websiteEntry.get()
    with open(file="Login_Info.json", mode="r") as file:
        data = json.load(file)

        try:
            loginInfo = data[website]
        except KeyError:
            messagebox.showinfo(title="ERROR", message=f"No information found for \"{website}\"")
        else:
            username = loginInfo["Username"]
            password = loginInfo["Password"]
            messagebox.showinfo(title=f"Information found for {website}", message=f"Username: {username}\nPassword: {password}")



def addInfo():
    website = websiteEntry.get()
    email = emailEntry.get()
    password = passEntry.get()
    info: dict = {
        website: {
                "Username": email,
                "Password": password
            }
    }

    isReadyToSave = messagebox.askokcancel(title=website, message=f"Entering:\nUsername: {email}\nPassword: {password}")

    if isReadyToSave:
        outputFile = open(file="Login_Info.json", mode="r")
        data = json.load(outputFile)
        data.update(info)
        outputFile.close()

        outputFile = open(file="Login_Info.json", mode="w")
        json.dump(data, outputFile, indent=4)
        outputFile.close()
        websiteEntry.delete(0, END)
        passEntry.delete(0, END)





def generatePassword():
    passEntry.delete(0,END)
    password = passwordGenerator.generateRandomPassword()
    passEntry.insert(END, string=password)


websiteLabel = Label(text="Website:", font=(FONT_NAME, 12, "normal"))
websiteLabel.grid(column=0, row=1)

emailLabel = Label(text="Username:", font=(FONT_NAME, 12, "normal"))
emailLabel.grid(column=0, row=2)

passLabel = Label(text="Password:", font=(FONT_NAME, 12, "normal"))
passLabel.grid(column=0, row=3)

websiteEntry = Entry(width=21, highlightthickness=0)
websiteEntry.grid(column=1, row=1,)

searchButton = Button(text="Search", width=15, command=search)
searchButton.grid(column=2, row=1)

emailEntry = Entry(width=40, highlightthickness=0)
emailEntry.grid(column=1, row=2, columnspan=2)


passEntry = Entry(width=21, highlightthickness=0)
passEntry.grid(column=1, row=3)


genPass = Button(text="Generate Password", bg="gray", width=15, command=generatePassword)
genPass.grid(column=2, row=3)

addButton = Button(text="Add", width=37, command=addInfo)
addButton.grid(column=1, row=4, columnspan=2)




window.mainloop()
