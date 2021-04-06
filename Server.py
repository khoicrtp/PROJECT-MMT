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
    if login(client)==1:
        welcome = 'Welcome! If you ever want to quit, type {quit} to exit.' 
        client.send(bytes(welcome, "utf8"))
        while True:
            try:
                msg = client.recv(BUFSIZ)
                if msg != bytes("{quit}", "utf8"):  
                    print("Recieve message: "+ msg.decode("utf8"))
                    function(msg.decode("utf8"),client)
                else:
                    del clients[client]
                    client.close()
                    break
            except:
                continue
    else:
        register(client)

def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    for sock in clients:
        sock.send(bytes(prefix+" "+msg, "utf8"))

def login(client):
    client.send(
            bytes("Now type your username and password and press login!", "utf8"))
    log = client.recv(BUFSIZ).decode("utf8")
    split = log.split()
    user=split[1]
    pas=split[2]   
    if check_login(user,pas)==1:
        return 1
    return 0
def check_login(user, pas):
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
def register(client):
    handle_client(client)
if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()