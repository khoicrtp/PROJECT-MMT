import sqlite3

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
        dateW + "'" + ", " + "'" + minT + "'" + ", " + "'" + \
            maxT + "'" + ", " + "'" + s_id + "'"+")"

    cur.execute(query)
    con.commit()


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
                break
    return result


# def findInfo(con):

try:
    print("Successfully Connected to SQLite")
    # TEST CASE:
    #executeSQL(sqliteConnection, cursor, 'data.sql')
    #insertCity(sqliteConnection, cursor, "006", "Cam Ranh", "VietNam")
    insertWeather(sqliteConnection, cursor, "005", '2021-4-24', '30', '35', '2')
    #executeSQL(sqliteConnection, cursor, 'exec.sql')
    sqliteConnection.commit()

    #print(printAllSQL(sqliteConnection, cursor))

    #insertCity(sqliteConnection, cursor, '5', 'Washington')

    # for i in range(7):
    

    #print(printFindSQL(sqliteConnection, cursor, '004'))

    cursor.close()


except sqlite3.Error as error:
    print("Error while executing sqlite script", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection is closed")
