from tkinter import *
import tkinter as tkinter
from functools import partial
import os

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

def writeFileStr(strFile, str):
    file = open(strFile, "r")
    
    str+='\n'
    Lines = file.readlines()
    Lines.append(str)
    #print(Lines)
    file.close()
    
    file = open(strFile, "w")
    file.writelines(Lines)
    file.close()

def rewriteFile(strFile, a):
    file=open(strFile, "w")
    lines=[]
    for i in range(len(a)):
        lines.append(a[i][0]+" "+a[i][1])
    file.writelines(lines)
    file.close()

def viewNotepad(filename):
    os.system(filename)
    
def updateUserUI():
    def updateUser(usr,pwd):
        aUsers=getFile("user.txt")
        
        for i in range(len(aUsers)):
            if(aUsers[i][0]==usr.get()):
                aUsers[i][1]=pwd.get()
                rewriteFile("user.txt", aUsers)
                return    
        
        str=usr.get()+" "+pwd.get()
        print(str)
        writeFileStr("user.txt",str)
        

    
    ui = tkinter.Tk()
    ui.geometry("600x300")
    ui.title("UPDATE USER DATA")
    ui.configure(bg='light blue')
    
    usrLabel = tkinter.Label(
    ui, text="USERNAME", bg='pink').grid(row=0, column=0)
    usr = tkinter.StringVar()
    usrEntry = tkinter.Entry(
        ui, textvariable=usr).grid(row=0, column=1)
    
    pwdLabel = tkinter.Label(
    ui, text="PASSWORD", bg='pink').grid(row=1, column=0)
    pwd = tkinter.StringVar()
    pwdEntry = tkinter.Entry(
        ui, textvariable=pwd).grid(row=1, column=1)
    
    def updateCombined():
        updateUser(usr,pwd)
    
    def viewNotepadCombined():
        viewNotepad("user.txt")
        
    updateDataButton = tkinter.Button(
        ui, text="Update user data", bg='yellow', command=updateCombined).grid(row=5, column=1)
    viewNotepadButton = tkinter.Button(
        ui, text="View user data", bg='light green', command=viewNotepadCombined).grid(row=5, column=2)
    
    ui.mainloop()
    
#updateUserUI()

aUsers=getFile("user.txt")
print(aUsers)