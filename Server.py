#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
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
    for i in range(len(a)):
        lines.append(a[i][0]+" "+a[i][1])
    file.writelines(lines)
    file.close()


def login(usr, pwd):
    print("login--")
    aUsers = getFile("user.txt")
    for i in range(len(aUsers)):
        if(aUsers[i][0] == usr and aUsers[i][1] == pwd):
            return 1
    return 0


def function(client):
    client.send(
        bytes("Here is your data you're finding: ", "utf8"))


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
    print(aUsers)
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
    if code == "LS":
        if globalMsg != "{logout}":
            print("Recieve message: " + globalMsg)
            function(client)
     # L or R
    print(code)
    user = split[1]
    pas = split[2]
    print('user'+code)
    print(user)
    print(pas)
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


if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
