import sqlite3
import datetime
import random

sqliteConnection = sqlite3.connect('weather.db')
cursor = sqliteConnection.cursor()


def now():
    return datetime.datetime.now()


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


def updateWeather(con, cur, c_id, dateW, minT, maxT, s_id):
    query = "UPDATE WEATHER_DAILY SET MIN_TEMP=" + str(minT) + ", MAX_TEMP=" +\
            str(maxT) + ", S_ID=" + s_id + " WHERE C_ID=" + \
        "'" + c_id + "'" + " AND WDATE=" + "'" + dateW + "'"

    cur.execute(query)
    con.commit()


def insertWeather(con, cur, c_id, dateW, minT, maxT, s_id):
    try:
        query = "INSERT INTO WEATHER_DAILY(C_ID, WDATE, MIN_TEMP, MAX_TEMP, S_ID) VALUES (" + "'" + c_id + "'" + ", " + "'" + \
            dateW + "'" + ", " + "'" + str(minT) + "'" + ", " + "'" + \
                str(maxT) + "'" + ", " + "'" + s_id + "'"+")"

        cur.execute(query)
        con.commit()
    except:
        updateWeather(sqliteConnection, cursor,
                      "001", '2021-4-24', 30, 35, '3')


def generateWeatherData(con, cur):
    random.seed(1)
    for i in range(5):
        cid = '00'+str(i+1)
        today = now()
        for j in range(30):
            nextDay = datetime.datetime.today() + datetime.timedelta(days=j)
            dateW = str(nextDay.year)+"-"+str(nextDay.month) + \
                "-"+str(nextDay.day)
            #insertWeather(con, cur, cid,)
            deltaTemp = random.random()
            minT = str(round((35-deltaTemp-1)))
            maxT = str(round((35+deltaTemp+1)))
            sID = str(random.randint(1, 8))
            insertWeather(con, cur, cid, dateW, minT, maxT, sID)


def getWeather(con, cur):
    query = "SELECT DISTINCT* FROM WEATHER_DAILY D, WEATHER_STATUS S, CITY C WHERE D.C_ID=C.C_ID AND D.S_ID=S.S_ID"
    cur.execute(query)
    table = cursor.fetchall()
    return table


def getCity(con, cur):
    query = "SELECT* FROM CITY"
    cur.execute(query)
    table = cursor.fetchall()
    return table


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

    #print(printCity7Day(sqliteConnection, cursor, 'HaNoi'))
    #print(printAllCityInDay(sqliteConnection, cursor))
    #print(printAllCityInSpecifiedDay(sqliteConnection, cursor, '2021-4-24'))
    #insertCity(sqliteConnection, cursor, '5', 'Washington')

    #print(printAllCity(sqliteConnection, cursor))
    # ;print(printFindSQL(sqliteConnection, cursor, '004'))

    insertWeather(sqliteConnection, cursor, "001", '2021-4-24', 29, 35, '4')

    #generateWeatherData(sqliteConnection, cursor)
    cursor.close()


except sqlite3.Error as error:
    print("Error while executing sqlite script", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection is closed")
