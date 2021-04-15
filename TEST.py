from tkinter import *
import tkinter


class mainMaster:
    def __init__(self, master):
        self.master = master

        master.geometry("600x300")
        master.close_button = Button(
            master, text="Close", command=master.quit)
        master.close_button.pack()

        def combinedPrintAll():
            print("F ALL")
        #send_server("F ALL")

        master.listAllButton = Button(
            master, text="All weather data", bg="light green", command=combinedPrintAll)
        master.listAllButton.pack()

        master.findLabel = Label(
            master, text="City, date, weather,...")
        master.findLabel.pack()

        master.findVar = tkinter.StringVar()

        master.findEntry = Entry(
            master, textvariable=master.findVar)
        master.findEntry.pack()

        def sendFind(var):
            print(var)
            str = "F "+var.get()
            print(str)
            send_server(str)

        def combinedFind():
            # master.destroy()
            sendFind(findVar)

        master.findButton = Button(
            master, text="Find", bg="yellow", command=combinedFind)
        master.findButton.pack()

        def combinedLog():
            messagebox.showinfo(
                "Goodbye", "Thank you for using my team's app!")
            master.qmastert()

        master.logoutButton = Button(
            master, text="Logout", bg='orange', command=combinedLog)
        master.logoutButton.pack()

    def greet(self):
        print("Greetings!")

    def selfDes():
        master.quit()


root = Tk()
my_gmaster = mainMaster(root)
root.mainloop()

my_gmaster.selfDes()
