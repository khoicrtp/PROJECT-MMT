import tkinter.messagebox
from tkinter import *
from array import *
import tkinter
from functools import partial
import os


def printIndex(a, n):
    temp = ""
    for i in a[n]:
        temp += i
        temp += " "
    print(temp)

# print all row


def printAll():
    file = open('weather.txt')

    Lines = file.readlines()
# read 2D-array from Lines
    a = []
    tmp = ""
    for i in range(len(Lines)):
        tmp = Lines[i]
        split = tmp.split()
        a.append([(j) for j in split])
    result = ""
    for i in range(len(a)):
        for j in range(len(a[i])):
            result += a[i][j] + " "
        result += "\n"

    tkinter.messagebox.showinfo("WEATHER INFORMATION", result)


########################################
def getLogin():
    loginFile = open('user.txt')
    Lines = loginFile.readlines()

    aUsers = []
    tmp = ""
    for i in range(len(Lines)):
        tmp = Lines[i]
        split = tmp.split()
        aUsers.append([(j) for j in split])
    return aUsers

# ADMIN UI


def updateUser():
    os.system("user.txt")


def updateData():
    os.system("weather.txt")


def adminUI():
    ui = tkinter.Tk()
    ui.geometry("600x300")
    ui.title("ADMINISTRATOR")

    updateDataButton = tkinter.Button(
        ui, text="Update weather data", command=updateData).grid(row=0, column=0)
    changeUserButton = tkinter.Button(
        ui, text="Update user's info", command=updateUser).grid(row=0, column=1)

    def combinedLog():
        ui.destroy()
        mainUI()
    logoutButton = tkinter.Button(
        ui, text="Logout", command=combinedLog).grid(row=2, column=7)
    ui.mainloop()

# USER UI


def printFind(find):
    file = open('weather.txt')

    Lines = file.readlines()
# read 2D-array from Lines
    a = []
    tmp = ""
    result = ""
    for i in range(len(Lines)):
        tmp = Lines[i]
        split = tmp.split()
        a.append([(j) for j in split])
    for i in range(len(a)):
        for j in range(len(a[i])):
            if (a[i][j] == find.get()):
                for k in range(len(a[i])):
                    result += a[i][k] + " "
                result += '\n'

    tkinter.messagebox.showinfo("RESULT", result)


def writeToFile(a, str):
    fout = open(str)

    for i in a:
        fout.write(i)


def changeUserPass(username, password):
    aUsers = getLogin()
    for i in aUsers:
        if(i[0] == 'username'):
            i[1] = password
    writeToFile(aUsers, "login.txt")


def userUI():
    ui = tkinter.Tk()
    ui.geometry("600x300")
    ui.title("USER")

    listAllButton = tkinter.Button(
        ui, text="All weather data", command=printAll).grid(row=0, column=0)
    # findDataButton = tkinter.Button(
    #    ui, text="Find", command=findUI).grid(row=0, column=1)
    findLabel = tkinter.Label(
        ui, text="City, date, weather,...").grid(row=1, column=0)
    find = tkinter.StringVar()

    findEntry = tkinter.Entry(
        ui, textvariable=find).grid(row=1, column=3)

    validateFind = partial(printFind, find)

    findButton = tkinter.Button(
        ui, text="Find", command=validateFind).grid(row=1, column=7)

    def combinedLog():
        ui.destroy()
        mainUI()
    logoutButton = tkinter.Button(
        ui, text="Logout", command=combinedLog).grid(row=2, column=7)

    ui.mainloop()


# MAIN UI


def register(Rusername, Rpassword):
    info = open("user.txt", "r")
    Lines = info.readlines()

    print(Rusername.get())

    Lines.append("\n" + Rusername.get() + " " + Rpassword.get())

    fout = open("user.txt", "w")
    for i in range(len(Lines)):
        fout.write(Lines[i])
    tkinter.messagebox.showinfo("STATUS", "Registration completed!")


def register2(Rusername, Rpassword):
    info = open("user.txt", "r")
    Lines = info.readlines()

    print(Rusername)

    Lines.append(Rusername + " " + Rpassword)

    fout = open("user.txt", "w")
    for i in Lines:
        fout.write(i)
    tkinter.messagebox.showinfo("STATUS", "Registration completed!")


def registerUI():
    reg = tkinter.Tk()
    reg.geometry('400x150')

    reg.title('REGISTRATION')

# username label and text entry box
    RusernameLabel = tkinter.Label(reg, text="User Name").grid(row=0, column=0)
    Rusername = tkinter.StringVar()
    RusernameEntry = tkinter.Entry(
        reg, textvariable=Rusername).grid(row=0, column=1)

# password label and password entry box
    RpasswordLabel = tkinter.Label(reg, text="Password").grid(row=1, column=0)
    Rpassword = tkinter.StringVar()
    RpasswordEntry = tkinter.Entry(
        reg, textvariable=Rpassword, show='*').grid(row=1, column=1)

    validateReg = partial(register, Rusername, Rpassword)

    def combinedFunc():
        # validateReg
        register(Rusername, Rpassword)
        # register2(Rusername.get(), Rpassword.get())
        reg.destroy()
        mainUI()
# reg button
    regButton = tkinter.Button(
        reg, text="Register", command=combinedFunc).grid(row=4, column=0)

    reg.mainloop()

# MAIN UI


def mainUI():
    def Login(username, password):
        if((username.get()) == "a" and (password.get()) == "a"):
            tkinter.messagebox.showinfo(
                "WELCOME", "Welcome back, admin!")
        # CHẠY UI ADMIN
            mainUI.destroy()
            adminUI()
            return
        else:
            aUsers = getLogin()
            i = 0
            for i in range(len(aUsers)):
                if(aUsers[i][0] == username.get() and aUsers[i][1] == password.get()):
                    tkinter.messagebox.showinfo(
                        "WELCOME", "Welcome back "+username.get())
                    mainUI.destroy()
                # CHẠY UI USER
                    userUI()
                    return
                elif(aUsers[i][0] == username.get()):
                    tkinter.messagebox.showinfo(
                        "ERROR", "Wrong password! Please try again")
                if(i == len(aUsers)-1):
                    tkinter.messagebox.showinfo(
                        "ERROR", "Invalid Login info, please create a new one")
                    mainUI.destroy()
                    registerUI()
                    return

    mainUI = tkinter.Tk()
    mainUI.geometry('400x150')
    mainUI.title('LOGIN')

# username label and text entry box
    usernameLabel = tkinter.Label(
        mainUI, text="User Name").grid(row=0, column=0)
    username = tkinter.StringVar()
    usernameEntry = tkinter.Entry(
        mainUI, textvariable=username).grid(row=0, column=1)

# password label and password entry box
    passwordLabel = tkinter.Label(
        mainUI, text="Password").grid(row=1, column=0)
    password = tkinter.StringVar()
    passwordEntry = tkinter.Entry(
        mainUI, textvariable=password, show='*').grid(row=1, column=1)

    validateLogin = partial(Login, username, password)

# login button
    loginButton = tkinter.Button(
        mainUI, text="Login", command=validateLogin).grid(row=4, column=0)

    def combinedFunc():
        mainUI.destroy()
        registerUI()

    regButton = tkinter.Button(
        mainUI, text="Register", command=combinedFunc).grid(row=4, column=2)

    mainUI.mainloop()


# main()

mainUI()
