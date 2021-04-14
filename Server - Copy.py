#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import*
from threading import Thread
import tkinter

clients = {}    # list of names
addresses = {}

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65431        # Port to listen on (non-privileged ports are > 1023)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind((HOST, PORT))

BUFSIZ = 1024
ADDR = (HOST, PORT)
# login


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


def login(usr, pwd):
    msg_list.insert(tkinter.END, "login--")
    aUsers = getFile("user.txt")
    for i in range(len(aUsers)):
        if(aUsers[i][0] == usr and aUsers[i][1] == pwd):
            return 1
    return 0
# Register


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
        return 0

    Lines.append("\n" + Rusername.get() + " " + Rpassword.get())
    fout = open("user.txt", "w")
    for i in range(len(Lines)):
        fout.write(Lines[i])
    return 1


def checkValid(a, username):
    for i in range(len(a)):
        if (a[i][0] == username.get()):
            return 0
    return 1
# Function


def function(client, globalMsg):
    client.send(
        bytes("Here is your data you're finding: ", "utf8"))


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        str = client_address + ": has connected."
        msg_list.insert(tkinter.END, str)

        addresses[client] = client_address
        Thread(target=receive, args=(client,)).start()


def receive(client):
    globalMsg = ""
    aUsers = getFile("user.txt")
    while True:
        try:
            print(globalMsg)
            if globalMsg == "{quit}":
                print("%s:%s left." % addresses[client])
                del addresses[client]
                client.close()
                break
            if(len(globalMsg) != 0):
                handle_client(client, globalMsg)
                globalMsg = ""
            else:
                globalMsg = client.recv(BUFSIZ).decode("utf8")
        except OSError:
            break


def handle_client(client, globalMsg):  # Takes client socket as argument.
    """Handles a single client connection."""
    msg_list.insert(tkinter.END, globalMsg)
    split = globalMsg.split()
    code = split[0]
    if code == "F":
        if globalMsg != "logout":
            print("Recieve message: " + globalMsg)
            function(client)
     # L or R
    user = split[1]
    pas = split[2]
    if code == "L" and login(user, pas) == 1:
        print("OK")
        client.send(bytes("LS", "utf8"))
    elif code == "L" and login(user, pas) == 0:
        client.send(bytes("LUS", "utf8"))
    elif code == "R" and register(user, pas) == 0:
        client.send(bytes("RUS", "utf8"))
    elif code == "R" and register(user, pas) == 1:
        client.send(bytes("RS", "utf8"))
    else:
        client.send(bytes("C", "utf8"))


def serverUI():
    ui = tkinter.Tk()
    ui.title("Chatter")

    messages_frame = tkinter.Frame(ui)
    my_msg = tkinter.StringVar()  # For the messages to be sent.
    my_msg.set("Type your messages here.")
# To navigate through past messages.
    scrollbar = tkinter.Scrollbar(messages_frame)
# Following will contain the messages.
    msg_list = tkinter.Listbox(messages_frame, height=15,
                               width=50, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    msg_list.pack()
    messages_frame.pack()

    def randomNum():
        for i in range(100):
            msg_list.insert(tkinter.END, i)

    entry_field = tkinter.Entry(ui, textvariable=my_msg)
    entry_field.bind("<Return>")
    entry_field.pack()
    send_button = tkinter.Button(ui, text="Send", command=randomNum)
    send_button.pack()

    ui.mainloop()


def serverUI():
    ui = tkinter.Tk()
    ui.title("Chatter")

    messages_frame = tkinter.Frame(ui)
    my_msg = tkinter.StringVar()  # For the messages to be sent.
    my_msg.set("Type your messages here.")
# To navigate through past messages.
    scrollbar = tkinter.Scrollbar(messages_frame)
# Following will contain the messages.
    msg_list = tkinter.Listbox(messages_frame, height=15,
                               width=50, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    msg_list.pack()
    messages_frame.pack()

    def randomNum():
        for i in range(100):
            msg_list.insert(tkinter.END, i)

    entry_field = tkinter.Entry(ui, textvariable=my_msg)
    entry_field.bind("<Return>")
    entry_field.pack()
    send_button = tkinter.Button(ui, text="Send", command=randomNum)
    send_button.pack()

    ui.mainloop()


#
if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()

    serverUI()
    msg_list.insert(tkinter.END, "Waiting for connection...")