from array import *
import tkinter
from functools import partial
import os


file = open('weather.txt')
Lines = file.readlines()
# print all Lines
for i in Lines:
    print(i.strip())
# read 2D-array from Lines
a = []
tmp = ""
for i in range(len(Lines)):
    tmp = Lines[i]
    split = tmp.split()
    a.append([(j) for j in split])
print(a)
print('\n')

# print one row


def printIndex(a, n):
    temp = ""
    for i in a[n]:
        temp += i
        temp += " "
    print(temp)

# print all row


def printAll(a):
    for i in range(len(a)):
        printIndex(a, i)


printAll(a)
print('\n')


def printFind(a, str):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if (a[i][j] == str):
                printIndex(a, i)
    print('\n')


printFind(a, 'CamRanh')


########################################
def getLogin():
    loginFile = open('login.txt')
    Lines = loginFile.readlines()

    aUsers = []
    tmp = ""
    for i in range(len(Lines)):
        tmp = Lines[i]
        split = tmp.split()
        aUsers.append([(j) for j in split])
    return aUsers

# ADMIN UI

# ADMIN OPTION


def updateUser():
    os.system("user.txt")


def updateData():
    os.system("weather.txt")


def adminUI():
    tkWindow.quit()
    ui = tkinter.Tk()
    ui.geometry("400x150")
    ui.title("ADMINISTRATOR")

    updateDataButton = tkinter.Button(
        ui, text="Update weather data", command=updateData).grid(row=0, column=0)
    changeUserButton = tkinter.Button(
        ui, text="Update user's info", command=updateUser).grid(row=0, column=1)

    ui.mainloop()

# MAIN UI


def register(username, password):
    info = open("user.txt", "r")
    Lines = info.readlines()

    Lines.append("\n" + username + " " + password)

    fout = open("user.txt", "w")
    for i in Lines:
        fout.write(i)


def Login(username, password):
    if((username.get()) == "a" and (password.get()) == "a"):
        print("Hi admin!")
        # CHẠY UI ADMIN
        tkWindow.destroy()
        adminUI()
        return
    else:
        aUsers = getLogin()
        for i in range(len(aUsers)):
            if(aUsers[i][0] == username.get() and aUsers[i][1] == password.get()):
                print("Hi "+username.get())
                tkWindow.destroy()
                # CHẠY UI USER
                return
            elif(aUsers[i][0] == username.get()):
                print("The account has been used. Please create a new one.")
        print("Can't find the inputted user")
    return


# MAIN

register("newuws", "pass")


tkWindow = tkinter.Tk()
tkWindow.geometry('400x150')
tkWindow.title('LOGIN')

# username label and text entry box
usernameLabel = tkinter.Label(tkWindow, text="User Name").grid(row=0, column=0)
username = tkinter.StringVar()
usernameEntry = tkinter.Entry(
    tkWindow, textvariable=username).grid(row=0, column=1)

# password label and password entry box
passwordLabel = tkinter.Label(tkWindow, text="Password").grid(row=1, column=0)
password = tkinter.StringVar()
passwordEntry = tkinter.Entry(
    tkWindow, textvariable=password, show='*').grid(row=1, column=1)

validateLogin = partial(Login, username, password)

# login button
loginButton = tkinter.Button(
    tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)

tkWindow.mainloop()


# main()
