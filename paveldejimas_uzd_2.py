# Sukurti programą, kuri:

#     Turėtų klasę Darbuotojas
#     Darbuotojas turėtų savybes: vardas, valandos_ikainis, dirba_nuo
#     Turėtų privatų metodą kuris paskaičiuotų, kiek darbuotojas nudirbo dienų nuo įvestos dienos (dirba_nuo) iki šiandien (turint omeny, kad darbuotojas dirba 7 dienas per savaitę)
#     Turėtų metodą paskaiciuoti_atlyginima, kuris panaudodamas aukščiau aprašytu metodu, paskaičiuotų bendrą atlyginimą (turint omeny, kad darbuotojas dirba 8 valandas per dieną)
#     Turėtų klasę NormalusDarbuotojas, kuri pakeistų Darbuotojo klasę taip, kad ji skaičiuotų atlyginimą, dirbant darbuotojui 5 dienas per savaitę
#     Sukurti norimą Darbuotojo objektą
#     Sukurti norimą NormalusDarbuotojas objektą
#     Su abiem objektais paleisti funkciją paskaiciuoti_atlyginima

import datetime

class Darbuotojas():
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = dirba_nuo

    def kiek_dirba_dienu(self): 
        dabar = datetime.date.today()
        skirtumas = dabar - self.dirba_nuo
        return skirtumas.days   

    def kiek_dirba_valandu(self):
        dabar = datetime.date.today()
        skirtumas = dabar - self.dirba_nuo
        return skirtumas.days * 8

    def kiek_uzdirba(self):
        atlyginimas = self.valandos_ikainis * self.kiek_dirba_valandu()
        print(f"{self.vardas} uzdirbo: {str(atlyginimas)} euru")


class NormalusDarbuotojas(Darbuotojas):
    def kiek_dirba_valandu1(self):
       
        dabar = datetime.date.today()
        skirtumas = dabar - self.dirba_nuo
        return (skirtumas.days * 8) // 7 * 5   


laurynas = Darbuotojas("Laurynas", 10, datetime.date(2021, 9, 16))
mantas = NormalusDarbuotojas("Mantas", 15, datetime.date(2020, 9, 16))

print(laurynas.kiek_dirba_dienu())
print(laurynas.kiek_dirba_valandu())
print(mantas.kiek_dirba_valandu1())
laurynas.kiek_uzdirba()
mantas.kiek_uzdirba()



