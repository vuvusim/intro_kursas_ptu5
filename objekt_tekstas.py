# Parašyti klasę Sakinys, kuri turi savybę tekstas ir metodus, kurie:

#     Gražina tekstą atbulai
#     Gražina tekstą mažosiomis raidėmis
#     Gražina tekstą didžiosiomis raidėmis
#     Gražina žodį pagal nurodytą eilės numerį
#     Gražina, kiek tekste yra nurodytų simbolių arba žodžių
#     Gražina tekstą su pakeistu nurodytu žodžiu arba simboliu
#     Atspausdina, kiek sakinyje yra žodžių, skaičių, didžiųjų ir mažųjų raidžių

# Susikurti kelis klasės objektus ir išbandyti visus metodus

class Sakinys():
    def __init__(self, tekstas="Laba Diena. Kaip jum sekasi?"):
        self.tekstas = tekstas

    def __str__(self):
        return f"Jusu sakinys yra: {self.tekstas}"

    def tekstas_atbulai(self):
        return self.tekstas[::-1]

    def tekstas_mazosiomis(self):
        return self.tekstas.lower()

    def tekstas_didziosiomis(self):
        return self.tekstas.upper()

    def grazina_zodi(self, eiles_numeris): # turim susikurti nauja kintamaji kad patalpintume eiles numeri
        isskaidom = self.tekstas.split() # isskaidzius stringa tada ji sudeda is lista
        return isskaidom[eiles_numeris]

    def ieskomas(self, ieskomas): # susikuriam nauja kintamaji (ieskomas)
        return self.tekstas.count(ieskomas) # su count() funkcija prasome ivesti ieskomo simbolio ar zodzio

    def pakeistas(self, senas_zodis, naujas_zodis): # isirasom du naujus kintamuosius i kuriuos veliau idesim sena zodi ir nauja zodi ir tada juos pakeisime tekste
        return self.tekstas.replace(senas_zodis, naujas_zodis)

    def suskaiciuokim(self):
        zodziu_kiekis = len(self.tekstas.split())
        skaiciai = sum(i.isnumeric() for i in self.tekstas)
        didziosios = sum(i.isupper() for i in self.tekstas)
        mazosios = sum(i.islower() for i in self.tekstas)
        print(f"Zodziu kiekis: {zodziu_kiekis}\nSkaiciu kiekis: {skaiciai}\nDidziuju raidziu kiekis: {didziosios}\nMazuju raidziu kiekis: {mazosios}")



sakinys = Sakinys()
print(sakinys.tekstas_atbulai())
print(sakinys.tekstas_mazosiomis())
print(sakinys.tekstas_didziosiomis())
print(sakinys.grazina_zodi(1)) # turime butinai ivesti eiles numeri kad gautume rezultata
print(sakinys.ieskomas("a")) # spausdina kiek yra ieskomu simboliu duotame kintamajame
print(sakinys.pakeistas("Kaip", "Kiek")) # isirasom kokius zodzius ar simbolius norim pakeisti
sakinys.suskaiciuokim()
print(sakinys)








