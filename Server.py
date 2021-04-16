#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application.c"""
import tkinter
from socket import*
from threading import Thread

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
    aUsers = getFile("user.txt")
    for i in range(len(aUsers)):
        if(aUsers[i][0] == usr and aUsers[i][1] == pwd):
            return 1
    return 0
# Register


def checkValid(a, username):
    for i in range(len(a)):
        if (a[i][0] == username):
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
        return 0

    Lines.append("\n" + Rusername + " " + Rpassword)
    fout = open("user.txt", "w")
    for i in range(len(Lines)):
        fout.write(Lines[i])
    return 1


# Function


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
            if a[i][j] == find:
                for k in range(len(a[i])):
                    result += a[i][k] + " "
                result += '\n'
    return result


def function(client, info):
    msg = printFind(info)
    client.send(
        bytes("F "+msg, "utf8"))


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
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
    print(globalMsg)
    split = globalMsg.split()
    code = split[0]
    if code == "F":
        info = split[1]
        if info != "":
            print("Recieve message: " + info)
            function(client, info)
    else:
        # Login or Register
        try:
            user = split[1]
            pas = split[2]
            if code == "L":
                print("%s:%s : " % addresses[client]+"Receive username and password are "+user + " " + pas
                      + " to login")
                if login(user, pas) == 1:
                    client.send(bytes("LS", "utf8"))
                elif login(user, pas) == 0:
                    client.send(bytes("LUS", "utf8"))
            if code == "R":
                print("%s:%s : " % addresses[client]+"Receive username and password are " + user + " " + pas
                      + " to register")
                if register(user, pas) == 1:
                    client.send(bytes("RS", "utf8"))
                elif register(user, pas) == 0:
                    client.send(bytes("RUS", "utf8"))
        except:
            if code == "L":
                client.send(bytes("LUS", "utf8"))
            if code == "R":
                client.send(bytes("RUS", "utf8"))


def serverUI():
    global top


# def printServer(msg):
#    msg_list.insert(tkinter.END, msg)

if __name__ == "__main__":
    #UI_THREAD = Thread(target=serverUI)
    # UI_THREAD.start()
    top = tkinter.Tk()
    top.title("Chatter")
    messages_frame = tkinter.Frame(top)
    my_msg = tkinter.StringVar()  # For the messages to be sent.

# To navigate through past messages.
    scrollbar = tkinter.Scrollbar(messages_frame)
# Following will contain the messages.
    msg_list = tkinter.Listbox(messages_frame, height=15,
                               width=50)
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    msg_list.pack()
    messages_frame.pack()

    def printServer(msg):
        msg_list.insert(tkinter.END, msg)

    def test():
        for i in range(1000):
            #msg_list.insert(tkinter.END, i)
            printServer(i)

    send_button = tkinter.Button(top, text="Test", command=test)
    send_button.pack()

    SERVER.listen(5)
    msg_list.insert(tkinter.END, "Waiting for connection...")

    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    top.mainloop()
    SERVER.close()
