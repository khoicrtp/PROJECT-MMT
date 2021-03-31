# import everything from tkinter module
from tkinter import *

# import messagebox from tkinter module
import tkinter.messagebox

# create a tkinter root window
root = tkinter.Tk()

# root window title and dimension
root.title("When you press a button the message will pop up")
root.geometry('500x300')

# Create a messagebox showinfo
result = ""

def onClick():
    tkinter.messagebox.showinfo("SEARCH RESULT",  result)


# Create a Button
button = Button(root, text="Click Me", command=onClick, height=5, width=10)

# Set the position of button on the top of window.
button.pack(side='bottom')
root.mainloop()

from datetime import date, datetime, timedelta
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  port="3307",
  user="user",
  password="pass",
)

mycursor = mydb.cursor()

mycursor.execute("DROP database IF EXISTS weather")

mycursor.execute("CREATE DATABASE WEATHER")

mycursor.execute("USE WEATHER")
#mycursor.execute("SHOW DATABASES")
#for x in mycursor:
#  print(x)

mycursor.execute("DROP table IF EXISTS CITY")
mycursor.execute("DROP table IF EXISTS WEATHER_STATUS")
mycursor.execute("DROP table IF EXISTS WEATHER_DAILY")

mycursor.execute("CREATE TABLE CITY (City_ID char(8), name_city VARCHAR(255), country VARCHAR(255))")
mycursor.execute("CREATE TABLE WEATHER_STATUS (Status_ID int, name_status VARCHAR(255))")
mycursor.execute("CREATE TABLE WEATHER_DAILY (CT_ID char(8), cal_date date, min_temp int, max_temp int, ST_ID int)")

sql = "INSERT INTO CITY (name_city,City_ID, country) VALUES (%s, %s, %s)"
val = [("HaNoi", "001", "VietNam"), ("Sydney", "002", "Australia"), ("NewYork", "003", "American"), 
("Tokyo", "004", "Japan"), ("Berlin", "005", "German")]
mycursor.executemany(sql, val)

print(mycursor.rowcount, "was inserted.")

sql = "INSERT INTO WEATHER_STATUS (Status_ID, name_status) VALUES (%s, %s)"
val = [(1, "Rainy"), (2, "Sunny"), (3, "Cloudy"), (4, "Windy"), (5, "Partly cloudy"), (6, "Snowy"), 
(7, "Lightning"), (8, "Stormy")]
mycursor.executemany(sql, val)

print(mycursor.rowcount, "was inserted.")

sql = "INSERT INTO WEATHER_DAILY (CT_ID, cal_date, min_temp, max_temp, ST_ID) VALUES (%s, %s, %s, %s, %s)"
val = [("001", date(2021, 4, 24),30,35,2), ("001",date(2021, 4, 25),25,30,3), 
("001",date(2021, 4, 26),22,26,1), ("001",date(2021, 4, 27),23,28,4),("001",date(2021, 4, 28),25,30,3),
("001",date(2021, 4, 29),20,25,1), ("001",date(2021, 4, 30),25,29,4),]
mycursor.executemany(sql, val)

print(mycursor.rowcount, "was inserted.")

#mycursor.execute("SELECT * FROM WEATHER_DAILY")
#for x in mycursor:
#  print(x)

sql = "SELECT * from WEATHER_DAILY INNER JOIN CITY ON WEATHER_DAILY.CT_ID = CITY.City_ID JOIN WEATHER_STATUS ON WEATHER_DAILY.ST_ID= WEATHER_STATUS.Status_ID"

mycursor.execute(sql)

for x in mycursor:
  print(x)
  
mydb.close()
