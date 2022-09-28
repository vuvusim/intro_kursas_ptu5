from tkinter import *
from PIL import ImageTk, Image

langas = Tk()
paveiksliukas = ImageTk.PhotoImage(Image.open("img/python_darbas.png"))
panel = Label(langas, image=paveiksliukas)
panel.pack(side=BOTTOM, fill=BOTH, expand=YES)
langas.mainloop()
