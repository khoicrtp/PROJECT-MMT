#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application.c"""
from socket import*
from threading import Thread
import sqlite3
import datetime
clients = {}    # list of names
addresses = {}

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind((HOST, PORT))

BUFSIZ = 1024
ADDR = (HOST, PORT)

# SQL


def insertCity(con, cur, id, name, country):
    # append("%s:%s " % addresses[client]+" "+id + " " + name + " " + country)
    query = "INSERT INTO CITY(C_ID, C_NAME, COUNTRY) VALUES (" + \
        "'" + id + "'" + ", " + "'" + name + "'" + ", " + "'" + country + "'" ")"

    cur.execute(query)
    con.commit()


def insertWeather(con, cur, c_id, dateW, minT, maxT, s_id):

    query = "INSERT INTO WEATHER_DAILY(C_ID, WDATE, MIN_TEMP, MAX_TEMP, S_ID) VALUES (" + "'" + c_id + "'" + ", " + "'" + \
        dateW + "'" + ", " + "'" + minT + "'" + ", " + "'" + \
            maxT + "'" + ", " + "'" + s_id + "'"+")"

    cur.execute(query)
    con.commit()


def updateWeather(str, sqliteConnection, cursor):
    split = str.split()
    ID = split[0]
    date = split[1]
    min_temp = split[2]
    max_temp = split[3]
    S_ID = split[4]
    try:
        insertWeather(sqliteConnection, cursor, ID,
                      date, min_temp, max_temp, S_ID)
        sqliteConnection.commit()
        return 1
    except sqlite3.Error as error:
        print("Error while executing sqlite script", error)
        return 0
    return 0


def addCity(str, sqliteConnection, cursor):
    split = str.split()
    ID = split[0]
    name = split[1]
    country = split[2]
    try:
        insertCity(sqliteConnection, cursor, ID, name, country)
        sqliteConnection.commit()
        return 1
    except sqlite3.Error as error:
        print("Error while executing sqlite script", error)
        return 0
    return 0


def getWeather(con, cur):
    query = "SELECT DISTINCT* FROM WEATHER_DAILY D, WEATHER_STATUS S, CITY C WHERE D.C_ID=C.C_ID AND D.S_ID=S.S_ID"
    cur.execute(query)
    table = cur.fetchall()
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


def getCity(con, cur):
    query = "SELECT* FROM CITY"
    cur.execute(query)
    table = cur.fetchall()
    return table


def printAllCity(con, cur):
    result = ""
    table = getCity(con, cur)
    for i in table:
        result += str(i) + '\n'
    return result


def now():
    return datetime.datetime.now()


def findToArray(con, cur, data):
    # ('004', '2021-4-26', 22.0, 26.0, '1', '1', 'Rainy', '004', 'Tokyo', 'Japan')
    table = getWeather(con, cur)

    result = []

    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == data:
                result.append(table[i])
                break
    return result


def printWeatherArray(a):
    temp = ""
    for weather in a:
        temp += weather[8] + " " + weather[1] + " " + \
            str(weather[2]) + " " + str(weather[3]) + " " + weather[6] + '\n'
    return temp


def printCity7Day(con, cur, data):
    table = getWeather(con, cur)

    today = now()
    # 001, 2021-4-24, 30.0, 35.0, 2, 2, Sunny, 001, HaNoi, VietNam

    validDay = []
    for i in range(7):
        # print(str(today.year) + "-" +
        #      str(today.month) + "-" + str(today.day + i))
        validDay.append(str(today.year) + "-" +
                        str(today.month) + "-" + str(today.day + i))

    aCity = getCity(con, cur)

    result = ""
    listCityID = []
    for i in range(len(aCity)):
        listCityID.append(aCity[i][0])

    # print(listCityID)
    cityData = getCity(con, cur)
    for i in range(len(cityData)):
        temp = ""
        if(data in cityData[i]):
            aWeather = findToArray(con, cur, cityData[i][0])
            for weather in aWeather:
                cWeather = []
                if (weather[1] in validDay) and cityData[i][0] == weather[0]:
                    cWeather.append(weather)
                result += printWeatherArray(cWeather)
    return result


def printAllCityInDay(con, cur):
    table = getWeather(con, cur)

    today = now()
    # 001, 2021-4-24, 30.0, 35.0, 2, 2, Sunny, 001, HaNoi, VietNam

    validDay = (str(today.year) + "-" +
                str(today.month) + "-" + str(today.day))
    print(validDay)
    #validDay = '2021-4-24'
    aCity = getCity(con, cur)

    result = ""
    listCityID = []
    for i in range(len(aCity)):
        listCityID.append(aCity[i][0])

    # print(listCityID)

    for cid in listCityID:
        temp = ""
        aWeather = findToArray(con, cur, cid)
        for weather in aWeather:
            cWeather = []
            if (weather[1] == validDay) and cid == weather[0]:
                cWeather.append(weather)
                result += printWeatherArray(cWeather)
    return result


def printAllCityInSpecifiedDay(con, cur, validDay):
    table = getWeather(con, cur)

    aCity = getCity(con, cur)

    result = ""
    listCityID = []
    for i in range(len(aCity)):
        listCityID.append(aCity[i][0])

    # print(listCityID)

    for cid in listCityID:
        temp = ""
        aWeather = findToArray(con, cur, cid)
        for weather in aWeather:
            cWeather = []
            if (weather[1] == validDay) and cid == weather[0]:
                cWeather.append(weather)
                result += printWeatherArray(cWeather)
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
    writeFile("history.txt", str)


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
        bytes("FS "+msg, "utf8"))


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
    sqliteConnection = sqlite3.connect('weather.db')
    cursor = sqliteConnection.cursor()

    split = globalMsg.split()
    code = split[0]
    if code == "FIND":
        try:
            info = split[1]
            if info == "ALLCITYTODAY":
                client.send(
                    bytes("FS " + printAllCityInDay(sqliteConnection, cursor), "utf8"))
            elif info == "DAY":
                day = split[2]
                client.send(
                    bytes("FS " + printAllCityInSpecifiedDay(sqliteConnection, cursor, day), "utf8"))
            elif info == "CITY":
                city = split[2]
                client.send(
                    bytes("FS " + printCity7Day(sqliteConnection, cursor, city), "utf8"))
        except:
            client.send(
                bytes("FUS", "utf8"))
    elif code == "SHOW":
        info = split[1]
        append("%s:%s request to show " %
               addresses[client] + info)
        if info == "CITY":
            client.send(
                bytes("CITY " + printAllCity(sqliteConnection, cursor), "utf8"))
        elif info == "WEATHER":
            client.send(
                bytes("WEATHER " + printAllSQL(sqliteConnection, cursor), "utf8"))
    elif code == "UPDATE":
        append("%s:%s (ADMIN) request to update " %
               addresses[client] + " weather")
        try:
            msg = globalMsg[7:len(globalMsg)]
            if updateWeather(msg, sqliteConnection, cursor) == 1:
                client.send(bytes("US", "utf8"))
            elif updateWeather(msg, sqliteConnection, cursor) == 0:
                client.send(bytes("UUS", "utf8"))
        except:
            client.send(bytes("UUS", "utf8"))
    elif code == "ADD":
        append("%s:%s (ADMIN) request to add " % addresses[client] + " city")
        try:
            msg = globalMsg[4:len(globalMsg)]
            if addCity(msg, sqliteConnection, cursor) == 1:
                client.send(bytes("AS", "utf8"))
            elif addCity(msg, sqliteConnection, cursor) == 0:
                client.send(bytes("AUS", "utf8"))
        except:
            client.send(bytes("AUS", "utf8"))
    else:
        # Login or Register
        try:
            user = split[1]
            pas = split[2]
            if code == "L":
                append(
                    "%s:%s " % addresses[client]+"login username and password are "+user + " " + pas)
                if login(user, pas) == 1:
                    client.send(bytes("LS client", "utf8"))
                elif login(user, pas) == 2:
                    client.send(bytes("LS admin", "utf8"))
                elif login(user, pas) == 0:
                    client.send(bytes("LUS", "utf8"))
            if code == "R":
                append(
                    "%s:%s " % addresses[client]+"register username and password are "+user + " " + pas)
                if register(user, pas) == 1:
                    client.send(bytes("RS", "utf8"))
                elif register(user, pas) == 0:
                    client.send(bytes("RUS", "utf8"))
        except:
            if code == "L":
                client.send(bytes("LUS", "utf8"))
            if code == "R":
                client.send(bytes("RUS", "utf8"))

    cursor.close()
    sqliteConnection.close()


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

    # msg_list.insert(tkinter.END, msg)
    top.mainloop()


if __name__ == "__main__":
    SERVER.listen(5)
    append("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
    # file=open("history.txt","r+")
    # file.truncate(0)
    # file.close()
