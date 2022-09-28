from tkinter import Tk, Label

langas = Tk() # sukuriam lango objekta pagal Tk() klase

langas.geometry("500x300") # nustatom lango dydi    

uzrasas = Label(langas, text="Sveiki, studentai") # i langa sukuriam "uzrasas" objekta pagal Label klase su tekstu
uzrasas2 = Label(langas, text="Smagus antradienis")
uzrasas.pack() # supakuojam uzrasas (nuo sito momento uzrasas uzsirasys)
uzrasas2.pack(side="bottom")
langas.mainloop() # paleidzia lango programa



