import sqlite3
import datetime


sqliteConnection = sqlite3.connect('weather.db')
cursor = sqliteConnection.cursor()


def executeSQL(con, cur, filename):
    with open(filename) as sqlite_file:
        sql_script = sqlite_file.read()

        cursor.executescript(sql_script)
        print("SQLite script executed successfully")


def insertCity(con, cur, id, name, country):
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


def getWeather(con, cur):
    query = "SELECT DISTINCT* FROM WEATHER_DAILY D, WEATHER_STATUS S, CITY C WHERE D.C_ID=C.C_ID AND D.S_ID=S.S_ID"
    cursor.execute(query)
    table = cursor.fetchall()
    return table


def getCity(con, cur):
    query = "SELECT* FROM CITY"
    cursor.execute(query)
    table = cursor.fetchall()
    return table


def printAllCity(con, cur):
    table = getCity(con, cur)
    for i in table:
        print(i)


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
    for weather in a:
        print(weather[8] + " " + weather[1] +
              " " + str(weather[2]) + " " + str(weather[3]) + " " + weather[6])


def printAllSqlInDay(con, cur):
    table = getWeather(con, cur)

    today = now()
    # 001, 2021-4-24, 30.0, 35.0, 2, 2, Sunny, 001, HaNoi, VietNam

    validDay = []
    for i in range(7):
        print(str(today.year) + "-" +
              str(today.month) + "-" + str(today.day + i))
        validDay.append(str(today.year) + "-" +
                        str(today.month) + "-" + str(today.day + i))

    aCity = getCity(con, cur)

    result = ""
    listCityID = []
    for i in range(len(aCity)):
        listCityID.append(aCity[i][0])

    print(listCityID)

    for cid in listCityID:
        temp = ""
        aWeather = findToArray(con, cur, cid)
        for weather in aWeather:
            cWeather = []
            if (weather[1] in validDay) and cid == weather[0]:
                cWeather.append(weather)
                printWeatherArray(cWeather)
    return result


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
    # ('004', '2021-4-26', 22.0, 26.0, '1', '1', 'Rainy', '004', 'Tokyo', 'Japan')
    table = getWeather(con, cur)

    result = ""

    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == data:
                result += str(table[i]) + '\n'
                break
    return result


# def findInfo(con):

try:
    print("Successfully Connected to SQLite")

    # TEST CASE:
    #executeSQL(sqliteConnection, cursor, 'data.sql')
    #insertCity(sqliteConnection, cursor, "006", "Cam Ranh", "VietNam")
    #insertWeather(sqliteConnection, cursor, "003", stri, 30, 35, '2')
    #executeSQL(sqliteConnection, cursor, 'exec.sql')
    sqliteConnection.commit()

    #print(printAllSqlInDay(sqliteConnection, cursor))

    #insertCity(sqliteConnection, cursor, '5', 'Washington')

    print(printAllCity(sqliteConnection, cursor))
    # ;print(printFindSQL(sqliteConnection, cursor, '004'))

    cursor.close()


except sqlite3.Error as error:
    print("Error while executing sqlite script", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection is closed")
