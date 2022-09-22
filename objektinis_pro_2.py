# Sukurti klasę Sukaktis, kuri turėtų savybę data (galima atskirai įvesti metus, mėnesius ir kt.) ir metodus, kurie:

#     Gražina, kiek nuo įvestos sukakties praėjo metų, savaičių, dienų, valandų, minučių, sekundžių
#     Gražina, ar nurodytos sukakties metai buvo keliamieji
#     Atima iš nurodytos datos nurodytą kiekį dienų ir gražina naują datą
#     Prideda prie nurodytos datos nurodytą kiekį dienų ir gražina naują datą

import calendar

import datetime


class Sukaktis():
    def __init__(self, metai=1994, menuo=2, diena=19, valanda=15, minutes=3):
        self.metai = metai
        self.menuo = menuo
        self.diena = diena
        self.valanda = valanda
        self.minutes = minutes
        self.data = datetime.datetime(metai, menuo, diena, valanda, minutes)

    def kiek_praejo_laiko(self):   
        dabar = datetime.datetime.now()
        skirtumas = dabar - self.data
        print("Praejo metu: ", skirtumas.days // 365)
        print("Praejo menesiu: ", skirtumas.days // 365 * 12)
        print("Kiek praejo savaiciu: ", skirtumas.days // 7)   
        print("Kiek praejo dienu: ", skirtumas.days) 
        print("Kiek praejo valandu: ", skirtumas.total_seconds() // 3600)
        print("Kiek praejo minuciu: ", skirtumas.total_seconds() // 60)
        print("Kiek praejo sekundziu: ", skirtumas.total_seconds())

    def keliamieji_metai(self):
        if calendar.isleap(self.metai):
            print("Keliamieji metai")
        else:
            print("Nekeliamieji metai")

    def atima_dienas(self, dienos):
        return self.data - datetime.timedelta(days=dienos)

    def prideda_dienas(self, dienos):
        return self.data + datetime.timedelta(days=dienos)


data1 = Sukaktis(1888, 3, 15, 16, 30)
data1.kiek_praejo_laiko()
data1.keliamieji_metai()
print(data1.atima_dienas(10))
print(data1.prideda_dienas(10))