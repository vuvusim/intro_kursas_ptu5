from tkinter import *

langas = Tk()

text = StringVar()

def text_save():
    text.set(e_text.get())
    e_text.delete(0, len(e_text.get()))

def text_load():
    l_text["text"] = text.get()

def text_clear():
    # text.set("")
    l_text["text"] = ""
    e_text.delete(0, len(e_text.get()))

e_text = Entry(langas)
l_text = Label(langas, text="")
m_save = Button(langas, text="save", command=text_save)
m_load = Button(langas, text="load", command=text_load)
m_clear = Button(langas, text="clear", command=text_clear)
langas.bind("<Return>", lambda event: text_save())

e_text.pack()
l_text.pack(side=BOTTOM)
m_save.pack(side=LEFT)
m_load.pack(side=LEFT)
m_clear.pack(side=LEFT)

langas.mainloop()