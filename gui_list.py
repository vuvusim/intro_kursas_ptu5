from tkinter import *

langas = Tk()

def spausdinti():
    try:
        pasirinkta = sarasas[dezute.curselection()[0]]
    except IndexError:
        label_pasirinkta["text"] = "NIEKO!"
    else:
        label_pasirinkta["text"] = pasirinkta
        


slankiklis = Scrollbar(langas)
# listboxui priskiriam scrollbara, plotis 5, pasirinkti galima tik po viena
dezute = Listbox(langas, yscrollcommand=slankiklis.set, width=5, selectmode=SINGLE)
# scrollbaro pozicija atsinaujins, prastumus listboxa kitais budais (ne su scrollbaru)
slankiklis.config(command=dezute.yview)
sarasas = range(1983, 2023)
dezute.insert(END, *sarasas)
label_pasirinkta = Label(langas, text="Pasirinkite!")
button_pasirinkti = Button(langas, text="Rinktis", command=spausdinti)
dezute.pack(side=LEFT)
slankiklis.pack(side=RIGHT, fill=Y)
button_pasirinkti.pack()
label_pasirinkta.pack()
langas.mainloop()