#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application.c"""
from socket import*
from threading import Thread
import sqlite3


sqliteConnection = sqlite3.connect('weather.db')
cursor = sqliteConnection.cursor()

clients = {}    # list of names
addresses = {}

HOST = '192.168.106.129'  # Standard loopback interface address (localhost)
PORT = 7701        # Port to listen on (non-privileged ports are > 1023)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind((HOST, PORT))

BUFSIZ = 1024
ADDR = (HOST, PORT)

#SQL
sqliteConnection = sqlite3.connect('weather.db')
cursor = sqliteConnection.cursor()
def insertCity(con, cur, id, name, country):
    print(country)
    query = "INSERT INTO CITY(C_ID, C_NAME, COUNTRY) VALUES (" + \
        "'" + id + "'" + ", " + "'" + name + "'" + ", " + "'" + country + "'" ")"

    cur.execute(query)
    con.commit()
def insertWeather(con, cur, c_id, dateW, minT, maxT, s_id):
    query = "INSERT INTO WEATHER_DAILY(C_ID, WDATE, MIN_TEMP, MAX_TEMP, S_ID) VALUES (" + "'" + c_id + "'" + ", " + "'" + \
        dateW + "'" + ", " + "'" + str(minT) + "'" + ", " + "'" + \
            str(maxT) + "'" + ", " + "'" + s_id + "'"+")"
    print(query)

    cur.execute(query)
    con.commit()
def updateWeather(st,client):
    split = globalMsg.split()
    ID = split[0]
    date = split[1]
    min_temp = split[2]
    max_temp = split[3]
    S_ID = split[4]    
    try:
        insertWeather(sqliteConnection, cursor, ID, date, min_temp, max_temp, S_ID)
        sqliteConnection.commit()
    except sqlite3.Error as error:
        print("Error while executing sqlite script", error)

def addCity(str,client):
    split = str.split()
    ID = split[0]
    name = split[1]
    country = split[2]
    append("%s:%s " % addresses[client]+" "+ID + " " + name + " " + country)
    try:
        insertCity(sqliteConnection, cursor, ID, name, country)
        sqliteConnection.commit()
        return 1
    except sqlite3.Error as error:
        print("Error while executing sqlite script", error)
        return 0
    return 0

def getWeather(con, cur):
    query = "SELECT* FROM WEATHER_DAILY D, WEATHER_STATUS S, CITY C WHERE D.C_ID=C.C_ID AND D.S_ID=S.S_ID"
    cursor.execute(query)
    table = cursor.fetchall()
    return table

def printAllSQL(con, cur):
    table = getWeather(con, cur)

    result = ""
    for i in range(len(table)):
        temp = ""
        for j in range(len(table[i])):
            temp += str(table[i][j]) + " "
        result += temp + '\n'
    return result


def printFindSQL(con, cur, data):
    table = getWeather(con, cur)

    result = ""

    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == data:
                result += str(table[i]) + '\n'
    return result
 
# login
# FILE
def writeFile(strFile, str):
    file = open(strFile, "r")
    str += '\n'
    Lines = file.readlines()
    Lines.append(str)
    # print(Lines)
    file.close()
    file = open(strFile, "w")
    file.writelines(Lines)
    file.close()
def append(str):
    writeFile("history.txt",str)
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
    aAdmins = getFile("admin.txt")
    for i in range(len(aAdmins)):
        if(aAdmins[i][0] == usr and aAdmins[i][1] == pwd):
            return 2
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
        append("%s:%s has connected." % client_address)
        addresses[client] = client_address
        Thread(target=receive, args=(client,)).start()


def receive(client):
    globalMsg = ""
    aUsers = getFile("user.txt")
    while True:
        try:
            if globalMsg == "{quit}":
                append("%s:%s left." % addresses[client])
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
    if code == "FIND":
        info = split[1]
        if info != "":
            append("%s:%s request to find " % addresses[client] + info+ " weather")
            function(client, info)
    elif code=="UPDATE":
        append("%s:%s (ADMIN) request to update " % addresses[client] + " weather")
        msg=globalMsg[7:len(globalMsg)]
        if updateWeather(msg,client)==1:
            client.send(bytes("US", "utf8"))
        elif updateWeather(msg,client)==1:
            client.send(bytes("UUS", "utf8"))
    elif code=="ADD":
        append("%s:%s (ADMIN) request to add " % addresses[client] + " city")
        msg=globalMsg[4:len(globalMsg)]
        if addCity(msg,client)==1:
            client.send(bytes("AS", "utf8"))
        elif addCity(msg,client)==0:
            client.send(bytes("AUS", "utf8"))
    else:
        # Login or Register
        try:
            user = split[1]
            pas = split[2]
            if code == "L":
                append("%s:%s " % addresses[client]+"login username and password are "+user + " " + pas)
                if login(user, pas) == 1:
                    client.send(bytes("LS client", "utf8"))
                elif login(user, pas) == 2:
                    client.send(bytes("LS admin", "utf8"))
                elif login(user, pas) == 0:
                    client.send(bytes("LUS", "utf8"))
            if code == "R":
                append("%s:%s " % addresses[client]+"register username and password are "+user + " " + pas)
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

    send_button = tkinter.Button(top, text="Test", command=test)
    send_button.pack()

    #msg_list.insert(tkinter.END, msg)
    top.mainloop()

if __name__ == "__main__":
    SERVER.listen(5)
    append("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
    #file=open("history.txt","r+")
    #file.truncate(0)
    #file.close()
    
