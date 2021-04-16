import sqlite3

sqliteConnection = sqlite3.connect('weather.db')
cursor = sqliteConnection.cursor()


def executeSQL(con, cur, filename):
    with open(filename) as sqlite_file:
        sql_script = sqlite_file.read()

        cursor.executescript(sql_script)
        print("SQLite script executed successfully")


def insertCity(con, cur, id, name):
    query = "INSERT INTO CITY(ID, C_NAME) VALUES (" + \
        "'" + id + "'" + ", " + "'" + name + "'" + ")"


def insertWeather(con, cur, dateW, c_id, stat, temperature, ):
    query = "INSERT INTO WEATHER(WDATE, C_ID, WSTATE, TEMP, ) VALUES (" + "'" + id + "'" + ", " + "'" + \
        city + "'" + ", " + "'" + stat + "'" + ", " + "'" + \
            temperature + "'" + ", " + "'" + dateW + "'"+")"
    print(query)

    cur.execute(query)
    con.commit()


def getWeather(con, cur):
    query = "SELECT* FROM weather"
    cursor.execute(query)
    table = cursor.fetchall()
    return table


try:
    print("Successfully Connected to SQLite")

    # with open('TESTSQL.sql') as sqlite_file:
    #    sql_script=sqlite_file.read()

    #    cursor.executescript(sql_script)
    #    print("SQLite script executed successfully")

    # query="INSERT INTO weather(id,city,stat,temperature,dateW) VALUES (1,'HCM','Hot','30.1',datetime('now'))"

    # insertWeather(sqliteConnection, cursor, '3', 'Cam Ranh',
    #              'Cold', '29.3', '2021-04-16')
    executeSQL(sqliteConnection, cursor, 'TESTSQL.sql')

    table = getWeather(sqliteConnection, cursor)

    for i in range(len(table)):
        temp = ""
        for j in range(len(table[i])):
            temp += str(table[i][j]) + " "
        print(temp)

    insertCity('5', 'Washington')

    for i in range(7):
        insertWeather(sqliteConnection, cursor, '5', 'Washington', 'Cold',
                      '28.5', str('2021-04-'+str(17+i)))

    cursor.close()


except sqlite3.Error as error:
    print("Error while executing sqlite script", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection is closed")
