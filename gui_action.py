from tkinter import *

langas = Tk()

def spausdinti_su_enter():
    print("spausdina paspaudus ENTER")

def spausdinti_su_kairiu(event):
    print("spausdina paspaudus kairi")

def spausdinti_su_desiniu(event):
    print("spausdina paspaudus desini")


mygtukas = Button(langas, text="spausdinti")  #command=spausdinti
mygtukas.bind("<Button-1>", spausdinti_su_kairiu)
mygtukas.bind("<Button-3>", spausdinti_su_desiniu)
langas.bind("<Return>", lambda event: spausdinti_su_enter())
mygtukas.pack()
langas.mainloop()