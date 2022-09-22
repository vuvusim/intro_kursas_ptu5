# Sukurti programą, kuri:

#     Turėtų klasę Automobilis

#     Automobilis turėtų savybes: metai, modelis, kuro_tipas

#     Automobilis turėtų metodus: vaziuoti, stoveti, pildyti_degalu, kurie atitinkamai atspausdintų „Važiuoja“, „Priparkuota“, „Degalai įpilti“

#     Sukūrus objektą, automatiškai atspausdintų automobilio metus, modelį ir kuro tipą

#     Turėtų klasę Elektromobilis (jo tėvinis objektas – Automobilis)

#     Elektromobilis pakeistų Automobilio metodą pildyti_degalu taip, kad jis atspausdintų „Baterija įkrauta“

#     Elektromobilis turėtų metodą vaziuoti_autonomiskai, kuris spausdintų „Važiuoja autonomiškai“

#     Sukurti norimą Automobilio objektą

#     Sukurti norimą Elektromobilio objektą

#     Su sukurtu Automobilio objektu paleisti funkcijas vaziuoti, stoveti, pildyti_degalu

#     Su sukurtu Elektromobilio objektu paleisti funkcijas vaziuoti, stoveti, pildyti_degalu, vaziuoti_autonomiskai

from time import sleep

class Automobilis:

    def __init__(self, metai, modelis, kuro_tipas, kuro_bakas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        self.kuro_bakas = kuro_bakas
        self._informacija()

    def vaziuoti(self):
        for km in sorted(range(0, 50), reverse=True):
            print(f"Vaziuojam! Tau liko {km} litrai bake")
            sleep(0.2)
        else:
            print("Baigesi kuras")
            
        

    def stoveti(self):
        print("Priparkuota")


    def pildyti_degalu(self):
        kuro_bakas = int(input("Kiek litru norite pripilti kuro?: "))
        if kuro_bakas == 50:
            print("Degalai ipilti")
        if kuro_bakas < 50 or kuro_bakas > 50:
            print("Turi pilti pilna baka!")
       
       

    def _informacija(self):
        print("Metai:", self.metai, "Modelis:", self.modelis, "Tipas:", self.kuro_tipas, "Bako talpa:", self.kuro_bakas)


class Elektromobilis(Automobilis):

    def pildyti_degalu(self):
        for baterija in range(380, 481):
            print(f"Baterija kraunasi {baterija}")
        print("Baterija ikrauta")

    def vaziuoti_autonomiskai(self):
        for vaziuoja in sorted(range(380, 481), reverse=True):
            print(f"Vaziuojam! Tau liko {vaziuoja} V bake")
            sleep(0.1)
        print("Vaziuoja autonomiskai")


        

# automobilis = Automobilis(1996, "Kregzde", "Benzinas", 50)
automobilis1 = Elektromobilis(2020, "Tesla", "Elektra", 480)

# automobilis.pildyti_degalu()
# automobilis.vaziuoti()
# automobilis.stoveti()


automobilis1.pildyti_degalu()
automobilis1.vaziuoti_autonomiskai()




