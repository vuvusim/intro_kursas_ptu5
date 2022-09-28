from tkinter import *
from calendar import isleap

langas = Tk()


def spausdinti():
    ivesta = e_langelis.get()
    if int(ivesta) % 4 == 0 and (int(ivesta) % 100 != 0 or int(ivesta) % 400 == 0):
        l_rezultatas["text"] = (f"{ivesta} metai yra keliamieji")
    else:
        l_rezultatas["text"] = (f"{ivesta} metai nera keliamieji")
    


l_zodis = Label(langas, text="Iveskite metus")
e_langelis = Entry(langas)
mygtukas = Button(langas, text="Patvirtinti", command=spausdinti)
langas.bind("<Return>", lambda e: spausdinti())
l_rezultatas = Label(langas, text="")

l_zodis.grid(row=0, column=0)
e_langelis.grid(row=0, column=1)
mygtukas.grid(row=0, column=2)
l_rezultatas.grid(row=1, columnspan=3)

langas.mainloop()