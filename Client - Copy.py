#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
from socket import *
from threading import Thread
import tkinter
from array import *
import tkinter
from tkinter import messagebox
#from functools import partial
import os
import datetime

globalMsg = ""

########################################


def send_server(str):  # event is passed by binders.
    """Handles sending of messages."""
    client_socket.sendall(bytes(str, "utf8"))


# def on_closing(event=None):
    """This function is to be called when the window is closed."""
    # send_server("{quit}")
    # client_socket.close()


def userUI():
    ui = tkinter.Tk()
    ui.geometry("600x300")
    ui.title("USER")

    def combinedPrintAll():
        send_server("F ALL")
    listAllButton = tkinter.Button(
        ui, text="All weather data", bg="light green", command=combinedPrintAll).grid(row=0, column=0)

    findLabel = tkinter.Label(
        ui, text="City, date, weather,...").grid(row=1, column=0)
    findVar = tkinter.StringVar()

    findEntry = tkinter.Entry(
        ui, textvariable=findVar).grid(row=1, column=3)

    def sendFind(var):
        print(var.get())
        str = "F "+var.get()
        print(str)
        send_server(str)

    def combinedFind():
        ui.destroy()
        sendFind(findVar)

    findButton = tkinter.Button(
        ui, text="Find", bg="yellow", command=combinedFind).grid(row=1, column=7)

    def combinedLog():
        tkinter.messagebox.showinfo(
            "Goodbye", "Thank you for using my team's app!")
        ui.destroy()
        mainUI()

    logoutButton = tkinter.Button(
        ui, text="Logout", bg='orange', command=combinedLog).grid(row=2, column=7)

    ui.mainloop()


def mainUI():
    def sendLogin(username, password):
        str = "L "+username.get() + " " + password.get()
        print(str)
        send_server(str)

    mainUI = tkinter.Tk()
    mainUI.geometry('600x300')
    mainUI.title('LOGIN')
    mainUI.configure(bg='#ffc0cb')

    welcomeLabel = tkinter.Label(
        mainUI, text="WELCOME TO WEATHER APP", bg='light blue').grid(row=0, column=0)

# username label and text entry box
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

    #validateLogin = partial(sendLogin, username, password)
    def combinedLog():
        mainUI.destroy()
        sendLogin(username, password)
        # modeFilter(globalMsg)

# login button
    loginButton = tkinter.Button(
        mainUI, text="Login", bg="yellow", command=combinedLog).grid(row=1, column=2)

    def combinedReg():
        mainUI.destroy()
        # modeFilter(globalMsg)
        registerUI()

    regButton = tkinter.Button(
        mainUI, text="Register", bg="orange", command=combinedReg).grid(row=2, column=2)
    #mainUI.protocol("WM_DELETE_WINDOW", on_closing)
    mainUI.mainloop()


def modeFilter(str):
    split = str.split()
    code = split[0]
    if code == "LS":
        # HIDE THE WINDOW BEFORE
        master = tkinter.Tk()
        master.withdraw()

        tkinter.messagebox.showinfo("STATUS", "LOGIN SUCCESSFULLY")
        userUI()
        return 1
    elif code == "LUS":
        master = tkinter.Tk()
        master.withdraw()

        tkinter.messagebox.showinfo("STATUS", "LOGIN UNSUCCESSFULLY")
        return 1
    elif code == "RS":
        master = tkinter.Tk()
        master.withdraw()

        tkinter.messagebox.showinfo("STATUS", "REGISTER SUCCESSFULLY")
        # userUI()
        return 1
    elif code == "RUS":
        master = tkinter.Tk()
        master.withdraw()

        tkinter.messagebox.showinfo("STATUS", "REGISTER UNSUCCESSFULLY")
        return 1
    elif code == "F":
        master = tkinter.Tk()
        master.withdraw()

        tkinter.messagebox.showinfo("INFOMATION", str[2:len(str)])
        return 1


def receive():
    """Handles receiving of messages."""
    while True:
        try:
            global globalMsg

            if(len(globalMsg) != 0):
                msg = globalMsg
                globalMsg = ""
                modeFilter(msg)
            else:
                globalMsg = client_socket.recv(BUFSIZ).decode("utf8")

            #tkinter.messagebox.showinfo("GET ", globalMsg)

        except OSError:
            break


# ----Now comes the sockets part----

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65431        # The port used by the server
BUFSIZ = 1024

if not PORT:
    1
    PORT = 33000
else:
    PORT = int(PORT)


# Create a TCP/IP socket
ADDR = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
server_address = (HOST, PORT)
receive_thread = Thread(target=receive)
receive_thread.start()

mainUI()
