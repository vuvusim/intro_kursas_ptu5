# Sukurti klasę Sukaktis, kuri turėtų savybę data (galima atskirai įvesti metus, mėnesius ir kt.) ir metodus, kurie:

#     Gražina, kiek nuo įvestos sukakties praėjo metų, savaičių, dienų, valandų, minučių, sekundžių
#     Gražina, ar nurodytos sukakties metai buvo keliamieji
#     Atima iš nurodytos datos nurodytą kiekį dienų ir gražina naują datą
#     Prideda prie nurodytos datos nurodytą kiekį dienų ir gražina naują datą
import calendar
import datetime

class Sukaktis():
    def __init__(self, metai=1990, menuo=3, diena=15, valanda=23, minute=55):
        self.metai = metai
        self.menuo = menuo
        self.diena = diena
        self.valanda = valanda
        self.minute = minute
        self.data = datetime.datetime(metai, menuo, diena, valanda, minute)
    
    
    def kiek_praejo_laiko(self):
        dabar = datetime.datetime.now()
        skirtumas = dabar - self.data
        print("Praejo metu: ", skirtumas.days // 365)
        print("Praejo menesiu: ", skirtumas.days // 365 * 12)
        print("Praejo savaiciu: " , skirtumas.days // 7)
        print("Praejo dienu: ", skirtumas.days)
        print("Praejo valandu: ", skirtumas.total_seconds() // 3600)
        print("Praejo minuciu: ", skirtumas.total_seconds() // 60)
        print("Praejo sekundziu: ", skirtumas.total_seconds())

    def keliamieji(self):
        if calendar.isleap(self.metai):
            print(f"{self.metai} buvo keliamieji")
        else:
            print(f"{self.metai} nebuvo keliamieji")

    def atima_dienu(self, diena): # jei mes norime kazka daryti su butent tik vienu kintamuoju tai mes ta kintamaji turime prirasyti prie self i ()
        return self.data - datetime.timedelta(days=diena)

    def prideda_dienu(self, diena):
        return self.data + datetime.timedelta(days=diena)





data = Sukaktis()
data.kiek_praejo_laiko()
data.keliamieji()
print(data.atima_dienu(5))
print(data.prideda_dienu(5))








