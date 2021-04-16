import sqlite3
from array import *
import tkinter
from tkinter import messagebox
from functools import partial
import os
import datetime


def printIndex(a, n):
    temp = ""
    for i in a[n]:
        temp += i
        temp += " "
    print(temp)


# SQL

sqliteConnection = sqlite3.connect('weatherTest.db')
cursor = sqliteConnection.cursor()


def executeSQL(con, cur, filename):
    with open(filename) as sqlite_file:
        sql_script = sqlite_file.read()

        cursor.executescript(sql_script)
        print("SQLite script executed successfully")


def insertWeather(con, cur, id, city, stat, temperature, dateW):
    query = "INSERT INTO weather(id, city, stat, temperature, dateW) VALUES (" + "'" + id + "'" + ", " + "'" + \
        city + "'" + ", " + "'" + stat + "'" + ", " + "'" + \
            temperature + "'" + ", " + "'" + dateW + "'"+")"
    print(query)

    cur.execute(query)
    con.commit()


def getWeather(con, cur):
    query = "SELECT* FROM weather"
    cursor.execute(query)
    table = cursor.fetchall()
    return table


# ULTILITY
def printAllSQL():
    table = getWeather(sqliteConnection, cursor)

    result = ""
    for i in range(len(table)):
        temp = ""
        for j in range(len(table[i])):
            temp += str(table[i][j]) + " "
        # print(temp)
        result += temp+'\n'
    print(result)
    return(result)


def printFindSQL(find):
    a = getWeather(sqliteConnection, cursor)
    result = ''
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == find.get():
                for k in range(len(a[i])):
                    result += str(a[i][k]) + " "
                result += '\n'
    print(result)
    return result


def printAll():
    file = open('weather.txt')

    Lines = file.readlines()
    # read 2D-array from Lines
    a = []
    tmp = ""
    for i in range(len(Lines)):
        tmp = Lines[i]
        split = tmp.split()
        a.append([j for j in split])
    result = ""
    for i in range(len(a)):
        for j in range(len(a[i])):
            result += a[i][j] + " "
        result += "\n"

    tkinter.messagebox.showinfo("WEATHER INFORMATION", result)

# FILE


def getFile(filename):
    loginFile = open(filename)
    Lines = loginFile.readlines()

    aUsers = []
    tmp = ""
    for i in range(len(Lines)):
        tmp = Lines[i]
        split = tmp.split()
        aUsers.append([(j) for j in split])

    loginFile.close()
    return aUsers


def writeFile(strFile, str):
    file = open(strFile, "r")

    str += '\n'
    Lines = file.readlines()
    Lines.append(str)
    # print(Lines)
    file.close()

    file = open(strFile, "w")
    file.writelines(Lines)
    file.close()


def rewriteFile(strFile, a):
    file = open(strFile, "w")
    lines = []
    for i in range(len(a)-1):
        lines.append(a[i][0]+" "+a[i][1]+'\n')
    lines.append(a[len(a)-1][0]+" "+a[len(a)-1][1])
    file.writelines(lines)
    file.close()

# ADMIN UI


def viewNotepad(filename):
    os.system(filename)


def getFile(filename):
    loginFile = open(filename)
    Lines = loginFile.readlines()

    aUsers = []
    tmp = ""
    for i in range(len(Lines)):
        tmp = Lines[i]
        split = tmp.split()
        aUsers.append([(j) for j in split])

    loginFile.close()
    return aUsers


def writeFileStr(strFile, str):
    file = open(strFile, "r")

    Lines = file.readlines()
    Lines.append(str)
    # print(Lines)
    file.close()

    file = open(strFile, "w")
    file.writelines(Lines)
    file.close()


def updateWeatherUI():
    def updateWeather(id, city, weather, date):
        str = '\n' + id.get()+" "+city.get()+" "+weather.get()+" "+date.get()
        print(str)
        writeFileStr("weather.txt", str)
    
    ui = tkinter.Tk()
    ui.geometry("600x300")
    ui.title("UPDATE WEATHER DATA")
    ui.configure(bg='light blue')

    IDLabel = tkinter.Label(
        ui, text="ID", bg='pink').grid(row=0, column=0)
    ID = tkinter.StringVar()
    IDEntry = tkinter.Entry(
        ui, textvariable=ID).grid(row=0, column=1)

    cityLabel = tkinter.Label(
        ui, text="City", bg='pink').grid(row=1, column=0)
    city = tkinter.StringVar()
    cityEntry = tkinter.Entry(
        ui, textvariable=city).grid(row=1, column=1)

    weatherLabel = tkinter.Label(
        ui, text="Weather", bg='pink').grid(row=2, column=0)
    weather = tkinter.StringVar()
    weatherEntry = tkinter.Entry(
        ui, textvariable=weather).grid(row=2, column=1)

    dateLabel = tkinter.Label(
        ui, text="Date", bg='pink').grid(row=3, column=0)
    date = tkinter.StringVar()
    dateEntry = tkinter.Entry(
        ui, textvariable=date).grid(row=3, column=1)

    def updateCombined():
        updateWeather(ID, city, weather, date)

    def viewNotepadCombined():
        viewNotepad("weather.txt")

    def backCombined():
        ui.destroy()
        adminUI()

    updateDataButton = tkinter.Button(
        ui, text="Update weather data", bg='yellow', command=updateCombined).grid(row=5, column=1)
    viewNotepadButton = tkinter.Button(
        ui, text="View data", bg='light green', command=viewNotepadCombined).grid(row=5, column=2)
    backButton = tkinter.Button(
        ui, text="Back", bg='orange', command=backCombined).grid(row=5, column=3)

    ui.mainloop()


def updateUserUI():
    def updateUser(usr, pwd):
        aUsers = getFile("user.txt")

        for i in range(len(aUsers)):
            if(aUsers[i][0] == usr.get()):
                aUsers[i][1] = pwd.get()
                rewriteFile("user.txt", aUsers)
                return

        str = '\n' + usr.get()+" "+pwd.get()
        print(str)
        writeFileStr("user.txt", str)

    ui = tkinter.Tk()
    ui.geometry("600x300")
    ui.title("UPDATE USER DATA")
    ui.configure(bg='light blue')

    usrLabel = tkinter.Label(
        ui, text="USERNAME", bg='pink').grid(row=0, column=0)
    usr = tkinter.StringVar()
    usrEntry = tkinter.Entry(
        ui, textvariable=usr).grid(row=0, column=1)

    pwdLabel = tkinter.Label(
        ui, text="PASSWORD", bg='pink').grid(row=1, column=0)
    pwd = tkinter.StringVar()
    pwdEntry = tkinter.Entry(
        ui, textvariable=pwd).grid(row=1, column=1)

    def updateCombined():
        updateUser(usr, pwd)

    def viewNotepadCombined():
        viewNotepad("user.txt")

    def backCombined():
        ui.destroy()
        adminUI()

    updateDataButton = tkinter.Button(
        ui, text="Update user data", bg='yellow', command=updateCombined).grid(row=5, column=1)
    viewNotepadButton = tkinter.Button(
        ui, text="View user data", bg='light green', command=viewNotepadCombined).grid(row=5, column=2)
    backButton = tkinter.Button(
        ui, text="Back", bg='orange', command=backCombined).grid(row=5, column=3)

    ui.mainloop()


def adminUI():
    ui = tkinter.Tk()
    ui.geometry("600x300")
    ui.title("ADMINISTRATOR")
    ui.configure(bg='light blue')

    def combinedLogout():
        ui.destroy()
        mainUI()

    def combinedUpdateWeather():
        ui.destroy()
        updateWeatherUI()

    def combinedUpdateUser():
        ui.destroy()
        updateUserUI()

    updateDataButton = tkinter.Button(
        ui, text="Update weather data", bg='yellow', command=combinedUpdateWeather).grid(row=0, column=0)

    changeUserButton = tkinter.Button(
        ui, text="Update user's info", bg='light green', command=combinedUpdateUser).grid(row=0, column=1)

    logoutButton = tkinter.Button(
        ui, text="Logout", bg='orange', command=combinedLogout).grid(row=0, column=10)

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
            if a[i][j] == find.get():
                for k in range(len(a[i])):
                    result += a[i][k] + " "
                result += '\n'

    tkinter.messagebox.showinfo("RESULT", result)


def writeToFile(a, str):
    fout = open(str)

    for i in a:
        fout.write(i)


def changeUserPass(username, password):
    aUsers = getFile("user.txt")
    for i in aUsers:
        if i[0] == 'username':
            i[1] = password
    writeToFile(aUsers, "login.txt")


def userUI():
    ui = tkinter.Tk()
    ui.geometry("600x300")
    ui.title("USER")
    ui.configure(bg='light blue')

    listAllButton = tkinter.Button(
        ui, text="All weather data", bg="light green", command=printAllSQL).grid(row=0, column=0)
    # findDataButton = tkinter.Button(
    #    ui, text="Find", command=findUI).grid(row=0, column=1)
    findLabel = tkinter.Label(
        ui, text="City, date, weather,...").grid(row=1, column=0)
    find = tkinter.StringVar()

    findEntry = tkinter.Entry(
        ui, textvariable=find).grid(row=1, column=3)

    def combinedPrintFind():
        printFindSQL(find)

    findButton = tkinter.Button(
        ui, text="Find", bg="yellow", command=combinedPrintFind).grid(row=1, column=7)

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
        if a[i][0] == username.get():
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
        if (Rusername.get() == '' or Rpassword == ''):
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
        if ((username.get()) == "a" and (password.get()) == "a"):
            tkinter.messagebox.showinfo(
                "WELCOME", "Welcome back, admin!")
            # CHẠY UI ADMIN
            mainUI.destroy()
            adminUI()
            return
        else:
            aUsers = getFile("user.txt")
            i = 0
            for i in range(len(aUsers)):
                if (aUsers[i][0] == username.get() and aUsers[i][1] == password.get()):
                    tkinter.messagebox.showinfo(
                        "WELCOME", "Welcome back " + username.get())
                    mainUI.destroy()
                    # CHẠY UI USER
                    userUI()
                    return
                elif (aUsers[i][0] == username.get()):
                    tkinter.messagebox.showerror(
                        "ERROR", "Wrong password! Please try again")
                if (i == len(aUsers) - 1):
                    tkinter.messagebox.showerror(
                        "ERROR", "Invalid Login info, please create a new one")
                    mainUI.destroy()
                    registerUI()
                    return

    mainUI = tkinter.Tk()
    mainUI.geometry('600x300')
    mainUI.title('LOGIN')
    mainUI.configure(bg='#ffc0cb')

    welcomeLabel = tkinter.Label(
        mainUI, text="WELCOME TO WEATHER APP", bg='light blue').grid(row=0, column=0)

    # username label and text entry box4
    usernameLabel = tkinter.Label(
        mainUI, text="Username", bg='pink').grid(row=1, column=0)
    username = tkinter.StringVar()
    usernameEntry = tkinter.Entry(
        mainUI, textvariable=username).grid(row=1, column=1)

    # password label and password entry box
    passwordLabel = tkinter.Label(
        mainUI, text="Password", bg='pink').grid(row=2, column=0)
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
        mainUI, text="Register", bg="orange", command=combinedFunc).grid(row=2, column=2)

    mainUI.mainloop()


# main()

mainUI()

# printAllSQL()
# printFindSQL('HCM')
