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
        client.send(
            bytes("Greetings from the cave!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""
    if login(client)==1:
        client.send(
            bytes("Now type your name", "utf8"))
        name = client.recv(BUFSIZ).decode("utf8")
        welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
        client.send(bytes(welcome, "utf8"))
        # msg = "%s has joined the chat!" % name
        # broadcast(bytes(msg, "utf8"))
        clients[client] = name
        while True:
            msg = client.recv(BUFSIZ)
            if msg:
                if msg != bytes("{quit}", "utf8"):  
                    print("Recieve message: "+ msg.decode("utf8"))
                    # broadcast(msg, name+": ")
                    function(msg,client)
                else:
                    #client.send(bytes("{quit}", "utf8"))
                    client.close()
                    del clients[client]  #name
                    remove(client)
                    # broadcast(bytes("%s has left the chat." % name, "utf8"))
                    break
            else:
                remove(client)
    else:
        register(client)

def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

def remove(client): 
    if client in clients: 
        clients.remove(client) 
def login(client):
    client.send(
            bytes("Now type your username and press enter!", "utf8"))
    username = client.recv(BUFSIZ).decode("utf8")
    client.send(
            bytes("Now type your password and press enter!", "utf8"))
    password = client.recv(BUFSIZ).decode("utf8")
    return 1
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