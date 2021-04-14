import tkinter


def serverUI():
    ui = tkinter.Tk()
    ui.title("Chatter")

    messages_frame = tkinter.Frame(ui)
    my_msg = tkinter.StringVar()  # For the messages to be sent.
    my_msg.set("Type your messages here.")
# To navigate through past messages.
    scrollbar = tkinter.Scrollbar(messages_frame)
# Following will contain the messages.
    msg_list = tkinter.Listbox(messages_frame, height=15,
                               width=50, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    msg_list.pack()
    messages_frame.pack()

    def randomNum():
        for i in range(100):
            msg_list.insert(tkinter.END, i)

    entry_field = tkinter.Entry(ui, textvariable=my_msg)
    entry_field.bind("<Return>")
    entry_field.pack()
    send_button = tkinter.Button(ui, text="Send", command=randomNum)
    send_button.pack()

    ui.mainloop()


# serverUI()


str = '123456'
print(str[2:len(str)])

print(str[2:4])
