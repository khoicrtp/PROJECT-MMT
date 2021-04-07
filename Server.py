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

def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()
        
def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""
    
    while True:
        log = client.recv(BUFSIZ).decode("utf8")
        try:
            if log=="{quit}":
                del clients[client]
                client.close()
                break
        except:
            break
        split = log.split()
        code = split[0] # L or R
        user=split[1]
        pas=split[2]
        if code=="L" and login(user, pas)==1:
            client.send(bytes("LS", "utf8"))
            while True:
                msg = client.recv(BUFSIZ).decode("utf8")
                if msg != "{logout}" :  
                    print("Recieve message: "+ msg)
                    function(msg,client)
                else:
                    break    
        
        elif code=="L" and login(user, pas)==0:  
            client.send(bytes("LUS", "utf8"))
        elif code=="R" and register(user, pas)==0:
            client.send(bytes("RUS", "utf8"))
        elif code=="R" and register(user, pas)==1:
            client.send(bytes("RS", "utf8"))
        else:
            client.send(bytes("C", "utf8"))

def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    for sock in clients:
        sock.send(bytes(prefix+" "+msg, "utf8"))

def login(user, pas):
    loginFile = open('user.txt')
    Lines = loginFile.readlines()
    aUsers = []
    tmp = ""
    for i in range(len(Lines)):
        tmp = Lines[i]
        split = tmp.split()
        aUsers.append([(j) for j in split])
    i = 0
    for i in range(len(aUsers)):
        if(aUsers[i][0] == user and aUsers[i][1] == pas):
            return 1
    return 0

def function(msg, client):
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

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()