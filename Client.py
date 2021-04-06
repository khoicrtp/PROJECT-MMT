#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
from socket import *
from threading import Thread
import tkinter
from array import *
import tkinter
from tkinter import messagebox
from functools import partial
import os
import datetime


def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            tkinter.messagebox.showinfo("GET ", msg)
        except OSError:  
            break

def send(str):  # event is passed by binders.
    """Handles sending of messages."""
    client_socket.sendall(bytes(str, "utf8"))
    if str == "{quit}":
        client_socket.close()
        

def on_closing(event=None):
    """This function is to be called when the window is closed."""  
    send("quit")

def mainUI():
    def sendLogin(username, password):
        str="L "+username.get() + " " + password.get()
        print(str)
        send(str)
    
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

    validateLogin = partial(sendLogin, username, password)

# login button
    loginButton = tkinter.Button(
        mainUI, text="Login", bg="yellow", command=validateLogin).grid(row=1, column=2)

    def combinedFunc():
        mainUI.destroy()
        registerUI()

    regButton = tkinter.Button(
        mainUI, text="Register", bg="orange", command=combinedFunc).grid(row=2, column=2)
    mainUI.protocol("WM_DELETE_WINDOW", on_closing)
    mainUI.mainloop()



#----Now comes the sockets part----

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