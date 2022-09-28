import tkinter as tk

class Pagrindinis:
    def __init__(self, master):
        self.master = master
        self.b_naujas_langas = tk.Button(
            self.master, text="\U0001F680 Naujas langas", 
            width=40, 
            command=self.new_window, 
            font=sriftas, 
            fg="#fc0", 
            bg="#630", 
            highlightbackground="#740",
            highlightcolor="#fd2")
    
        self.b_naujas_langas.bind("<Enter>", lambda event: self.on_enter())
        self.b_naujas_langas.bind("<Leave>", lambda event: self.on_leave())
        self.b_naujas_langas.pack()

    def on_enter(self):
        self.b_naujas_langas["bg"] = "#741"

    def on_leave(self):
        self.b_naujas_langas["bg"] = "#630"

    def new_window(self):
        self.vidinis = tk.Toplevel(self.master)
        self.app = Vidinis(self.vidinis)

class Vidinis:
    def __init__(self, master):
        self.master = master
        self.b_uzdaryti = tk.Button(self.master, text="\u2717 Uzdaryti", width=10, command=self.close_window, font=sriftas, fg="#f00")
        self.b_uzdaryti.pack()

    def close_window(self):
        self.master.destroy()



langas = tk.Tk()
sriftas = "Arial", 20, "normal"
programa = Pagrindinis(langas)
langas.mainloop()
        



























