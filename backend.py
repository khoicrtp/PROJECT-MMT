import tkinter.messagebox
from tkinter import *
from array import *
import tkinter
from functools import partial
import os
import datetime


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
    ui.configure(bg='light blue')

    updateDataButton = tkinter.Button(
        ui, text="Update weather data", bg='yellow', command=updateData).grid(row=0, column=0)
    changeUserButton = tkinter.Button(
        ui, text="Update user's info", bg='light green', command=updateUser).grid(row=0, column=1)

    def combinedLog():
        ui.destroy()
        mainUI()
    logoutButton = tkinter.Button(
        ui, text="Logout", bg='orange', command=combinedLog).grid(row=0, column=10)
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
    ui.configure(bg='light blue')

    listAllButton = tkinter.Button(
        ui, text="All weather data", bg="light green", command=printAll).grid(row=0, column=0)
    # findDataButton = tkinter.Button(
    #    ui, text="Find", command=findUI).grid(row=0, column=1)
    findLabel = tkinter.Label(
        ui, text="City, date, weather,...").grid(row=1, column=0)
    find = tkinter.StringVar()

    findEntry = tkinter.Entry(
        ui, textvariable=find).grid(row=1, column=3)

    validateFind = partial(printFind, find)

    findButton = tkinter.Button(
        ui, text="Find", bg="yellow", command=validateFind).grid(row=1, column=7)

    def combinedLog():
        tkinter.messagebox.showinfo(
            "Goodbye", "Thank you for using my team's app!")
        ui.destroy()
        mainUI()
    logoutButton = tkinter.Button(
        ui, text="Logout", bg='orange', command=combinedLog).grid(row=2, column=7)

    ui.mainloop()


# MAIN UI
def checkValid(a, username):
    for i in range(len(a)):
        if (a[i][0] == username.get()):
            return 0
    return 1


def register(Rusername, Rpassword):
    info = open("user.txt", "r")
    Lines = info.readlines()

    a = []
    tmp = ""
    result = ""
    for i in range(len(Lines)):
        tmp = Lines[i]
        split = tmp.split()
        a.append([(j) for j in split])

    if checkValid(a, Rusername) == 0:
        tkinter.messagebox.showinfo(
            "ERROR", "The username is registered. Please try with another username.")
        return 0

    Lines.append("\n" + Rusername.get() + " " + Rpassword.get())

    fout = open("user.txt", "w")
    for i in range(len(Lines)):
        fout.write(Lines[i])
    tkinter.messagebox.showinfo("STATUS", "Registration completed!")
    return 1


def registerUI():
    reg = tkinter.Tk()
    reg.geometry('600x300')
    reg.title('REGISTRATION')
    reg.configure(bg='light blue')

# username label and text entry box
    RusernameLabel = tkinter.Label(reg, text="Username").grid(row=0, column=0)
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
        if(Rusername.get() == '' or Rpassword == ''):
            tkinter.messagebox.showinfo(
                "ERROR", "Registration failed. Please check username and password again")
            return
        flag = register(Rusername, Rpassword)
        if flag == 1:
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
                    tkinter.messagebox.showerror(
                        "ERROR", "Wrong password! Please try again")
                if(i == len(aUsers)-1):
                    tkinter.messagebox.showerror(
                        "ERROR", "Invalid Login info, please create a new one")
                    mainUI.destroy()
                    registerUI()
                    return

    mainUI = tkinter.Tk()
    mainUI.geometry('600x300')
    mainUI.title('LOGIN')
    mainUI.configure(bg='light blue')

    welcomeLabel = tkinter.Label(
        mainUI, text="WELCOME TO WEATHER APP").grid(row=0, column=0)

# username label and text entry box
    usernameLabel = tkinter.Label(
        mainUI, text="Username").grid(row=1, column=0)
    username = tkinter.StringVar()
    usernameEntry = tkinter.Entry(
        mainUI, textvariable=username).grid(row=1, column=1)

# password label and password entry box
    passwordLabel = tkinter.Label(
        mainUI, text="Password").grid(row=2, column=0)
    password = tkinter.StringVar()
    passwordEntry = tkinter.Entry(
        mainUI, textvariable=password, show='*').grid(row=2, column=1)

    validateLogin = partial(Login, username, password)

# login button
    loginButton = tkinter.Button(
        mainUI, text="Login", bg="yellow", command=validateLogin).grid(row=1, column=2)

    def combinedFunc():
        mainUI.destroy()
        registerUI()

    regButton = tkinter.Button(
        mainUI, text="Register", bg="light green", command=combinedFunc).grid(row=2, column=2)

    mainUI.mainloop()


# main()

mainUI()
