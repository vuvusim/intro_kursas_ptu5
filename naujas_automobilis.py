class Automobilis():
    def __init__(self, metai, modelis, kuro_tipas, kuro_bakas=40, degalai=0, dugnas=0):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        self.kuro_bakas = kuro_bakas
        self.__degalai = degalai
        self.dugnas = dugnas
        self._informacija()

    @property
    def degalai(self):
        return self.__degalai

    @degalai.setter
    def degalai(self, naujas_kiekis):
        if naujas_kiekis < self.dugnas:
            print("kuro bake negali būti neigiamas kiekis degalų")
        elif naujas_kiekis > self.kuro_bakas:
            print(f"kuro bake negali būti daugiau negu {self.kuro_bakas} L degalų")
        else:
            self.__degalai = naujas_kiekis

    def vaziuoti(self):
        if self.degalai > self.dugnas:
            self.degalai -= 1
            print("Važiuoja")
        else:
            self.stoveti()

    def stoveti(self):
        print("Priparkuota")

    def pildyti_degalu(self, kiekis=20):
        if (self.kuro_bakas - self.dugnas) - self.degalai < kiekis:
            print(f"Negalima perpildyti bako ({self.kuro_bakas} L), kuriame dar yra {self.degalai} L")
        else:
            self.degalai += kiekis
            print(f"Įpilta {kiekis} L degalų")

    def _informacija(self):
        print("Metai:", self.metai, "Modelis:", self.modelis, "Tipas:", self.kuro_tipas)


class Elektromobilis(Automobilis):
    def __init__(self, metai, modelis, kuro_tipas, kuro_bakas=480, degalai=480, dugnas=340):
        super().__init__(metai, modelis, kuro_tipas, kuro_bakas, degalai, dugnas)

    # @property
    # def degalai(self):
    #     return self.__degalai

    # @degalai.setter
    # def degalai(self, naujas_kiekis):
    #     if naujas_kiekis < self.dugnas:
    #         print("baterija negali buti labiau iskrauta")
    #     elif naujas_kiekis > self.kuro_bakas:
    #         print(f"Baterija negali buti daugiau ikrauta negu {self.kuro_bakas} V")
    #     else:
    #         self.__degalai = naujas_kiekis

    # def pildyti_degalu(self, kiekis):
    #     if (self.kuro_bakas - self.dugnas) - self.degalai < kiekis:
    #         print(f"Negalima perkrauti baterijos ({self.kuro_bakas} V), kuriame dar yra {self.degalai} V")
    #     else:
    #         self.degalai += kiekis
    #         print(f"Baterija pakrauta {kiekis} V")

    

    def vaziuoti_automonomiškai(self):
        if self.degalai > self.dugnas:
            self.degalai -= 1
            print("Važiuoja")
        else:
            self.stoveti()

    def stoveti(self):
        print("Priparkuota")

toyota = Automobilis(2015, "Toyota Avensis", "Dyzelinas", degalai=5)
tesla = Elektromobilis(2018, "Telsla Model S", "Elektra")

# for km in range(6):
#     toyota.vaziuoti()
#     print(toyota.degalai)
# # toyota.stoveti()
# toyota.pildyti_degalu()
# for km in range(5):
#     toyota.vaziuoti()
#     print(toyota.degalai)

for km in sorted(range(380, 390), reverse=True):
    tesla.vaziuoti_automonomiškai()
    print(tesla.degalai)

tesla.pildyti_degalu()
for km in sorted(range(480, 380), reverse=True):
    tesla.vaziuoti()
    print(tesla.degalai)

