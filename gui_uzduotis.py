from tkinter import *

langas = Tk()
meniu = Menu(langas)
langas.config(menu=meniu)
sub_meniu1 = Menu(meniu, tearoff=0)

paskutinis = StringVar()

def pasisveikinimas():
    ivesta = ivedimas1.get()
    uzrasas2["text"] = (f"Labas, {ivesta}")
    status["text"] = "Sukurta"
    paskutinis.set(uzrasas2["text"])

def isvalyti():
    uzrasas2["text"] = ""
    status["text"] = "Isvalyta"
    
def atkurti():
    uzrasas2["text"] = ivedimas1.get()
    status["text"] = "Atkurta"

def iseiti():
    langas.destroy()

meniu.add_cascade(label="Meniu", menu=sub_meniu1)
sub_meniu1.add_command(label="Isvalyti", command=isvalyti)
sub_meniu1.add_command(label="Atkurti", command=atkurti)
sub_meniu1.add_separator()
sub_meniu1.add_command(label="Iseiti", command=iseiti)


uzrasas1 = Label(langas, text="Iveskite varda")
ivedimas1 = Entry(langas)
mygtukas1 = Button(langas, text="Patvirtinti", command=pasisveikinimas)
langas.bind("<Return>", lambda e: pasisveikinimas())
langas.bind("<Escape>", lambda e: iseiti())
uzrasas2 = Label(langas, text="")
status = Label(langas, text="", bd=1, relief=SUNKEN, anchor=W)

uzrasas1.grid(row=0, column=0)
ivedimas1.grid(row=0, column=1)
mygtukas1.grid(row=0, column=2)
uzrasas2.grid(row=1, columnspan=3)
status.grid(row=2, columnspan=3, sticky=W+E)

langas.mainloop()