from socket import *
from threading import Thread
import tkinter
from array import *
import tkinter
from tkinter import messagebox
#from functools import partial
import os
import datetime
import time
import os

globalMsg = ""
flag = 0
FLAG = 0

########################################


def send_server(str):  # event is passed by binders.
    """Handles sending of messages."""
    client_socket.sendall(bytes(str, "utf8"))


def registerUI():
    reg = tkinter.Tk()
    reg.geometry('600x300')
    reg.title('REGISTRATION')
    reg.configure(bg='light blue')

    # username label and text entry box
    RusernameLabel = tkinter.Label(
        reg, text="Username").pack()  # .grid(row=0, column=0)
    Rusername = tkinter.StringVar()
    RusernameEntry = tkinter.Entry(
        reg, textvariable=Rusername).grid(row=0, column=1)

    # password label and password entry box
    RpasswordLabel = tkinter.Label(
        reg, text="Password").pack()  # .grid(row=1, column=0)
    Rpassword = tkinter.StringVar()
    RpasswordEntry = tkinter.Entry(
        reg, textvariable=Rpassword, show='*').pack()  # .grid(row=1, column=1)

    def sendRegister(Rusername, Rpassword):
        str = "R "+Rusername.get() + " " + Rpassword.get()
        # print(str)
        send_server(str)

    def combinedFunc():
        sendRegister(Rusername, Rpassword)
        time.sleep(2)
        reg.destroy()
    # reg button
    regButton = tkinter.Button(
        reg, text="Register", command=combinedFunc).pack()  # .grid(row=0, column=7)

    def combinedLog():
        global flag
        flag = 0
        reg.destroy()

    logoutButton = tkinter.Button(
        reg, text="Login", bg='orange', command=combinedLog).pack()  # .grid(row=1, column=7)

    def combinedClose():
        send_server("{quit}")
        client_socket.close()
        global flag
        flag = -1
        reg.destroy()

    closeButton = tkinter.Button(
        reg, text="EXIT", bg="red", command=combinedClose).pack()  # .grid(row=2, column=7)

    def on_closing():
        """This function is to be called when the window is closed."""
        send_server("{quit}")
        client_socket.close()
        global flag
        flag = -1
        reg.destroy()
    reg.protocol("WM_DELETE_WINDOW", on_closing)
    reg.mainloop()


def updateWeatherUI():
    def updateWeather(ID, date, min_temp, max_temp, S_ID):
        str = 'UPDATE ' + ID.get()+" "+date.get()+" "+min_temp.get() + \
            " "+max_temp.get()+" "+S_ID.get()
        # print(str)
        send_server(str)

    ui = tkinter.Tk()
    ui.geometry("600x300")
    ui.title("UPDATE WEATHER DATA")
    ui.configure(bg='light blue')

    IDLabel = tkinter.Label(
        ui, text="City_ID", bg='pink').pack()  # .grid(row=0, column=0)
    ID = tkinter.StringVar()
    IDEntry = tkinter.Entry(
        ui, textvariable=ID).pack()  # .grid(row=0, column=1)

    dateLabel = tkinter.Label(
        ui, text="Date", bg='pink').pack()  # .grid(row=1, column=0)
    date = tkinter.StringVar()
    dateEntry = tkinter.Entry(
        ui, textvariable=date).pack()  # .grid(row=1, column=1)

    min_tempLabel = tkinter.Label(
        ui, text="Min_temp", bg='pink').pack()  # .grid(row=2, column=0)
    min_temp = tkinter.StringVar()
    min_tempEntry = tkinter.Entry(
        ui, textvariable=min_temp).pack()  # .grid(row=2, column=1)

    max_tempLabel = tkinter.Label(
        ui, text="Max_temp", bg='pink').pack()  # .grid(row=3, column=0)
    max_temp = tkinter.StringVar()
    max_tempEntry = tkinter.Entry(
        ui, textvariable=max_temp).pack()  # .grid(row=3, column=1)

    S_IDLabel = tkinter.Label(
        ui, text="S_ID", bg='pink').pack()  # .grid(row=4, column=0)
    S_ID = tkinter.StringVar()
    S_IDEntry = tkinter.Entry(
        ui, textvariable=S_ID).pack()  # .grid(row=4, column=1)

    def updateCombined():
        updateWeather(ID, date, min_temp, max_temp, S_ID)

    updateDataButton = tkinter.Button(
        ui, text="Update weather data", bg='yellow', command=updateCombined).pack()  # .grid(row=5, column=1)

    def showStatCombined():
        send_server("SHOW STATUS")

    showStatButton = tkinter.Button(
        ui, text="SHOW STATUS", bg='yellow', command=showStatCombined).pack()  # .grid(row=6, column=1)

    def backCombined():
        global flag
        flag = 3
        ui.destroy()

    backButton = tkinter.Button(
        ui, text="Back", bg='orange', command=backCombined).pack()  # .grid(row=5, column=3)

    def combinedClose():
        send_server("{quit}")
        client_socket.close()
        global flag
        flag = -1
        ui.destroy()

    closeButton = tkinter.Button(
        ui, text="EXIT", bg="red", command=combinedClose).pack()  # .grid(row=5, column=8)

    def on_closing():
        """This function is to be called when the window is closed."""
        send_server("{quit}")
        client_socket.close()
        global flag
        flag = -1
        ui.destroy()
    ui.protocol("WM_DELETE_WINDOW", on_closing)
    ui.mainloop()


def addCityUI():
    def addCity(id, city, country):
        str = 'ADD ' + id.get()+" "+city.get()+" "+country.get()
        # print(str)
        send_server(str)

    ui = tkinter.Tk()
    ui.geometry("600x300")
    ui.title("UPDATE CITY INFO")
    ui.configure(bg='light blue')
    IDLabel = tkinter.Label(
        ui, text="City_ID", bg='pink').pack()  # .grid(row=0, column=0)
    ID = tkinter.StringVar()
    IDEntry = tkinter.Entry(
        ui, textvariable=ID).pack()  # .grid(row=0, column=1)

    cityLabel = tkinter.Label(
        ui, text="City_Name", bg='pink').pack()  # .grid(row=1, column=0)
    city = tkinter.StringVar()
    cityEntry = tkinter.Entry(
        ui, textvariable=city).pack()  # .grid(row=1, column=1)

    countryLabel = tkinter.Label(
        ui, text="Country", bg='pink').pack()  # .grid(row=2, column=0)
    country = tkinter.StringVar()
    countryEntry = tkinter.Entry(
        ui, textvariable=country).pack()  # .grid(row=2, column=1)

    def updateCombined():
        addCity(ID, city, country)
    updateDataButton = tkinter.Button(
        ui, text="Update city data", bg='yellow', command=updateCombined).pack()  # .grid(row=4, column=1)

    def showCityCombined():
        send_server("SHOW CITY")

    showCityButton = tkinter.Button(
        ui, text="Show city data", bg='green', command=showCityCombined).pack()  # .grid(row=5, column=1)

    def backCombined():
        global flag
        flag = 3
        ui.destroy()

    backButton = tkinter.Button(
        ui, text="Back", bg='orange', command=backCombined).pack()  # .grid(row=4, column=3)

    def combinedClose():
        send_server("{quit}")
        client_socket.close()
        global flag
        flag = -1
        ui.destroy()

    closeButton = tkinter.Button(
        ui, text="EXIT", bg="red", command=combinedClose).pack()  # .grid(row=5, column=8)

    def on_closing():
        """This function is to be called when the window is closed."""
        send_server("{quit}")
        client_socket.close()
        global flag
        flag = -1
        ui.destroy()
    ui.protocol("WM_DELETE_WINDOW", on_closing)

    ui.mainloop()


def adminUI():
    admin = tkinter.Tk()
    admin.geometry("600x300")
    admin.title("ADMINISTRATOR")
    admin.configure(bg='light blue')

    def combinedAddCity():
        global flag
        flag = 5
        admin.destroy()
        # addCityUI()
        #addCity(ID, city, country)

    addCityButton = tkinter.Button(
        admin, text="Add City", bg='pink', command=combinedAddCity).pack()  # grid(row=0, column=7)

    def combinedUpdateWeather():
        global flag
        flag = 4
        admin.destroy()

    updateDataButton = tkinter.Button(
        admin, text="Update weather data", bg='yellow', command=combinedUpdateWeather).pack()  # .grid(row=2, column=7)

    # changeUserButton = tkinter.Button(
    #    admin, text="Update user's info", bg='light green', command=combinedUpdateUser).grid(row=0, column=1)

    def combinedLog():
        tkinter.messagebox.showinfo(
            "Goodbye", "Thank you for using my team's app!")
        global flag
        flag = 0
        admin.destroy()

    logoutButton = tkinter.Button(
        admin, text="Logout", bg='orange', command=combinedLog).pack()  # .grid(row=3, column=7)

    def combinedClose():
        send_server("{quit}")
        client_socket.close()
        global flag
        flag = -1
        admin.destroy()

    closeButton = tkinter.Button(
        admin, text="EXIT", bg="red", command=combinedClose).pack()  # .grid(row=4, column=7)

    def on_closing():
        """This function is to be called when the window is closed."""
        send_server("{quit}")
        client_socket.close()
        global flag
        flag = -1
        admin.destroy()
    admin.protocol("WM_DELETE_WINDOW", on_closing)
    admin.mainloop()


def userUI():
    ui = tkinter.Tk()
    ui.geometry("600x300")
    ui.title("USER")

    def combinedPrintAll():
        send_server("FIND ALLCITYTODAY")

    listAllButton = tkinter.Button(
        ui, text="Weather Today Of All City", bg="light green", command=combinedPrintAll).pack()  # .grid(row=0, column=0)

    DayLabel = tkinter.Label(
        ui, text="DAY: ").pack()  # .grid(row=1, column=0)
    Day = tkinter.StringVar()

    DayEntry = tkinter.Entry(
        ui, textvariable=Day).pack()  # .grid(row=1, column=3)

    CityLabel = tkinter.Label(
        ui, text="CITY: ").pack()  # .grid(row=2, column=0)
    City = tkinter.StringVar()

    CityEntry = tkinter.Entry(
        ui, textvariable=City).pack()  # .grid(row=2, column=3)

    def sendDay(var):
        str = "FIND DAY "+var.get()
        # print(str)
        send_server(str)

    def combinedDay():
        # ui.destroy()
        sendDay(Day)

    findDayButton = tkinter.Button(
        ui, text="Find Day", bg="yellow", command=combinedDay).pack()  # .grid(row=1, column=7)

    def sendCity(var):
        # print(var)
        str = "FIND CITY "+var.get()
        send_server(str)

    def combinedCity():
        # ui.destroy()
        sendCity(City)

    findCityButton = tkinter.Button(
        ui, text="Find City", bg="yellow", command=combinedCity).pack()  # .grid(row=2, column=7)

    def combinedLog():
        tkinter.messagebox.showinfo(
            "Goodbye", "Thank you for using my team's app!")
        global flag
        flag = 0
        ui.destroy()

    logoutButton = tkinter.Button(
        ui, text="Logout", bg='orange', command=combinedLog).pack()  # .grid(row=3, column=7)

    def combinedClose():
        send_server("{quit}")
        client_socket.close()
        global flag
        flag = -1
        ui.destroy()

    closeButton = tkinter.Button(
        ui, text="EXIT", bg="red", command=combinedClose).pack()  # .grid(row=4, column=7)

    def on_closing():
        """This function is to be called when the window is closed."""
        send_server("{quit}")
        client_socket.close()
        global flag
        flag = -1
        ui.destroy()
    ui.protocol("WM_DELETE_WINDOW", on_closing)
    ui.mainloop()


def modeFilter(str):
    # print(str)
    split = str.split()
    code = split[0]
    master1 = tkinter.Tk()
    master1.withdraw()
    global flag
    if code == "LS":
        tkinter.messagebox.showinfo(
            "STATUS", "LOGIN SUCCESSFULLY", master=master1)
        who = split[1]
        if who == "admin":
            flag = 3
        elif who == "client":
            flag = 1
        return 1
    elif code == "LUS":
        tkinter.messagebox.showinfo(
            "STATUS", "LOGIN UNSUCCESSFULLY", master=master1)
        return 1
    elif code == "RS":
        tkinter.messagebox.showinfo(
            "STATUS", "REGISTER SUCCESSFULLY", master=master1)
        flag = 0
        return 1
    elif code == "RUS":
        tkinter.messagebox.showinfo(
            "STATUS", "REGISTER UNSUCCESSFULLY", master=master1)
        return 1
    elif code == "FS":
        tkinter.messagebox.showinfo(
            "INFOMATION", str[3:len(str)], master=master1)
        return 1
    elif code == "FUS":
        tkinter.messagebox.showinfo(
            "STATUS", "FIND UNSUCCESSFULLY", master=master1)
        return 1
    elif code == "US":
        tkinter.messagebox.showinfo(
            "STATUS", "UPDATE WEATHER SUCCESSFULLY", master=master1)
        return 1
    elif code == "UUS":
        tkinter.messagebox.showinfo(
            "STATUS", "UPDATE WEATHER UNSUCCESSFULLY", master=master1)
        return 1
    elif code == "AS":
        tkinter.messagebox.showinfo(
            "STATUS", "ADD CITY SUCCESSFULLY", master=master1)
        return 1
    elif code == "AUS":
        tkinter.messagebox.showinfo(
            "STATUS", "ADD CITY UNSUCCESSFULLY", master=master1)
        return 1
    elif code == "CITY":
        tkinter.messagebox.showinfo(
            "SHOW CITY", str[5:len(str)], master=master1)
    elif code == "STATUS":
        tkinter.messagebox.showinfo(
            "SHOW STATUS", str[7:len(str)], master=master1)


def receive():
    """Handles receiving of messages."""
    while True:
        try:
            global globalMsg

            if(len(globalMsg) != 0):
                if(globalMsg == "{quit}"):
                    os.system("TASKKILL /F /IM python.exe")
                    time.sleep(5)
                else:
                    msg = globalMsg
                    globalMsg = ""
                    modeFilter(msg)
            else:
                globalMsg = client_socket.recv(BUFSIZ).decode("utf8")
        except OSError:
            break


def mainUI():
    def sendLogin(username, password):
        str = "L "+username.get() + " " + password.get()
        # print(str)
        send_server(str)

    mainUI = tkinter.Tk()
    mainUI.geometry('600x300')
    mainUI.title('LOGIN')
    mainUI.configure(bg='#ffc0cb')

    welcomeLabel = tkinter.Label(
        mainUI, text="WELCOME TO WEATHER APP", bg='light blue').pack()  # .grid(row=0, column=0)

# username label and text entry box
    usernameLabel = tkinter.Label(
        mainUI, text="Username", bg='pink').pack()  # .grid(row=1, column=0)
    username = tkinter.StringVar()
    usernameEntry = tkinter.Entry(
        mainUI, textvariable=username).pack()  # .grid(row=1, column=1)

# password label and password entry box
    passwordLabel = tkinter.Label(
        mainUI, text="Password", bg='pink').pack()  # .grid(row=2, column=0)
    password = tkinter.StringVar()
    passwordEntry = tkinter.Entry(
        mainUI, textvariable=password, show='*').pack()  # .grid(row=2, column=1)

    def combinedLog():
        usr = username
        pwd = password
        sendLogin(usr, pwd)
        time.sleep(2)
        mainUI.destroy()

# login button
    loginButton = tkinter.Button(
        mainUI, text="Login", bg="yellow", command=combinedLog).pack()  # .grid(row=1, column=2)

    def combinedReg():
        global flag
        flag = 2
        mainUI.destroy()

    regButton = tkinter.Button(
        mainUI, text="Register", bg="orange", command=combinedReg).pack()  # .grid(row=2, column=2)

    def combinedClose():
        send_server("{quit}")
        client_socket.close()
        global flag
        flag = -1
        mainUI.destroy()

    closeButton = tkinter.Button(
        mainUI, text="EXIT", bg="red", command=combinedClose).pack()  # .grid(row=3, column=2)

    def on_closing():
        """This function is to be called when the window is closed."""
        send_server("{quit}")
        client_socket.close()
        global flag
        flag = -1
        mainUI.destroy()
    mainUI.protocol("WM_DELETE_WINDOW", on_closing)
    mainUI.mainloop()

# ----Now comes the sockets part----


def handle_UI():
    global flag
    while flag != -1:
        # print(flag)
        if(flag == 0):
            mainUI()
        # print(flag)
        if(flag == 1):
            userUI()
        # print(flag)
        if(flag == 2):
            registerUI()
        if(flag == 3):
            adminUI()
        if(flag == 4):
            updateWeatherUI()
        if(flag == 5):
            addCityUI()


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432
BUFSIZ = 32768
client_socket = socket(AF_INET, SOCK_STREAM)
# Create a TCP/IP socket


def mainFunc(host, port):
    # HOST = '127.0.0.1'  # The server's hostname or IP address
    # PORT = 65431        # The port used by the server
    global HOST
    global PORT
    HOST = host
    PORT = port

    ADDR = (HOST, PORT)
    client_socket.connect(ADDR)
    server_address = (HOST, PORT)
    receive_thread = Thread(target=receive)
    receive_thread.start()

    UI_thread = Thread(target=handle_UI)
    UI_thread.start()


try:
    mainFunc(HOST, PORT)
except:
    def inputHostUI():
        reg = tkinter.Tk()
        reg.geometry('600x300')
        reg.title('INPUT HOST')
        reg.configure(bg='light blue')
    # username label and text entry box
        hostLabel = tkinter.Label(
            reg, text="HOST").pack()  # .grid(row=0, column=0)
        host = tkinter.StringVar()
        hostEntry = tkinter.Entry(
            reg, textvariable=host).pack()  # .grid(row=0, column=1)
    # password label and password entry box
        # .grid(row=1, column=0)
        portLabel = tkinter.Label(reg, text="PORT").pack()
        port = tkinter.StringVar()
        portEntry = tkinter.Entry(
            reg, textvariable=port, show='*').pack()  # .grid(row=1, column=1)

        def setSocket(hostname, portID):
            global HOST
            global PORT
            HOST = hostname.get()
            PORT = int(portID.get())

        def combinedFunc():
            setSocket(host, port)
            time.sleep(1)
            global FLAG
            FLAG = 1
            reg.destroy()
     # reg button
        setButton = tkinter.Button(
            reg, text="SET HOST", command=combinedFunc).pack()  # .grid(row=0, column=7)
        reg.mainloop()
    inputHostUI()
    if(FLAG == 1):
        mainFunc(HOST, PORT)


# mainUI()
# userUI()
