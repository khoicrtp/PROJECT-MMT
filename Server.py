#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import*
from threading import Thread

        
clients = {}
addresses = {}

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65431        # Port to listen on (non-privileged ports are > 1023)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind((HOST, PORT))
SERVER.listen(5)

BUFSIZ = 1024
ADDR = (HOST, PORT)

def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.sendall(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = client.recv(BUFSIZ).decode("utf8")
    welcome = "Welcome" +name+ " If you ever want to quit, type quit to exit."
    client.sendall(bytes(welcome, "utf8"))
    msg = (name + " has joined the chat!")
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("quit", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.sendall(bytes("quit", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes(name + " has left the chat.", "utf8"))
            break


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.sendall(bytes(prefix, "utf8")+msg)



if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()