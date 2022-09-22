# Padaryti minibiudžeto programą, kuri:

#     Leistų vartotojui įvesti pajamas
#     Leistų vartotojui įvesti išlaidas
#     Leistų vartotojui parodyti pajamų/išlaidų balansą
#     Leistų vartotojui parodyti biudžeto ataskaitą (visus pajamų ir išlaidų įrašus su sumomis)
#     Leistų vartotojui išeiti iš programos
from operator import attrgetter
import datetime

class Irasas():
    def __init__(self, suma):
        self.suma = suma
        

class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_info, data_laikas):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_info = papildoma_info
        self.data_laikas = data_laikas

class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga, data_laikas):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga
        self.data_laikas = data_laikas

class Biudzetas():
    zurnalas = []

    # def rusiavimas(biudzetas):
    #     return biudzetas.data_laikas
    # sorted_list = sorted(zurnalas, key=rusiavimas)

    def pajamos(self, suma, siuntejas, papildoma_info, data_laikas):
        pajamos = PajamuIrasas(suma, siuntejas, papildoma_info, data_laikas)
        self.zurnalas.append(pajamos)

    def islaidos(self,suma, atsiskaitymo_budas, isigyta_preke_paslauga, data_laikas):
        islaidos = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga, data_laikas)
        self.zurnalas.append(islaidos)

    def balansas(self):
        suma = 0
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                suma += irasas.suma
            if isinstance(irasas, IslaiduIrasas):
                suma -= irasas.suma
        return suma

    def ataskaita(self):
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                print(f"Pajamos: {irasas.suma} {irasas.siuntejas} {irasas.papildoma_info} {irasas.data_laikas}")
            if isinstance(irasas, IslaiduIrasas):
                print(f"Islaidos: {irasas.suma} {irasas.atsiskaitymo_budas} {irasas.isigyta_preke_paslauga} {irasas.data_laikas}")
    

biudzetas = Biudzetas()



while True:
    print("1 - Iveskite pajamas")
    print("2 - iveskite islaidas")
    print("3 - Perziureti balanas")
    print("4 - Perziureti ataskaita")
    print("9 - Iseiti")
    veiksmas = input()

    if veiksmas == "1":
        print("Iveskite")
        suma = int(input("Pajamos"))
        
        siuntejas = input("Siuntejas: ")
        papildoma_info = input("Papildoma informacija: ")
        data_laikas = datetime.datetime.now()
        biudzetas.pajamos(suma, siuntejas, papildoma_info, data_laikas)
        print("Ivesta Teisingai")

    if veiksmas == "2":
        print("Iveskite")
        suma = int(input("Islaidos: "))
        atsiskaitymo_budas = input("Atsiskaitymo budas: ")
        isigyta_preke_paslauga = input("Isigyta preke ar paslauga: ")
        data_laikas = datetime.datetime.now()
        biudzetas.islaidos(suma, atsiskaitymo_budas, isigyta_preke_paslauga, data_laikas)
        print("Ivesta teisingai")
    
    if veiksmas == "3":
        print(f"Biudzetas: {biudzetas.balansas()}")

    if veiksmas == "4":
        print(f"Ataskaita: {biudzetas.ataskaita()}")

    if veiksmas == "9":
        break












