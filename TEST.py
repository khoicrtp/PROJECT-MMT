import tkinter


def printServer(root, msg):
    msg_list.insert(tkinter.END, msg)


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

    def test():
        for i in range(1000):
            #msg_list.insert(tkinter.END, i)
            printServer(top, i)

    send_button = tkinter.Button(top, text="Test", command=test)
    send_button.pack()

    #msg_list.insert(tkinter.END, msg)
    top.mainloop()


def printServer(root, msg):
    msg_list.insert(tkinter.END, msg)
