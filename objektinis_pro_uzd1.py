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
    def __init__(self, tekstas="Laba diena. Kaip jum sekasi?"):
        self.tekstas = tekstas

    def atbulai(self):
        return self.tekstas[::-1]

    def mazosiomis(self):
        return self.tekstas.lower()

    def didziosiomis(self):
        return self.tekstas.upper()

    def atspausdinti_zodi(self, skaicius):
        suskirstymas = self.tekstas.split()
        return suskirstymas[skaicius]

    def simb_raid(self, ieskomas):
        return self.tekstas.count(ieskomas)

    def pakeisti(self, senas, naujas):
        return self.tekstas.replace(senas, naujas)

    def info(self):
        zodziu_kiekis = len(self.tekstas.split())
        skaiciai = sum(i.isnumeric()for i in self.tekstas)
        didziosios = sum(i.isupper() for i in self.tekstas)
        mazosios = sum(i.islower() for i in self.tekstas)
        print(f"Zodziu kiekis: {zodziu_kiekis}\nSkaiciu kiekis: {skaiciai}\nDidziuju raidziu kiekis: {didziosios}\nMazuju raidziu kiekis: {mazosios}")

    

    def __str__(self):
        return ("Tekstas: " + self.tekstas)

mano_sakinys = Sakinys()
print(mano_sakinys.atbulai())
print(mano_sakinys.mazosiomis())
print(mano_sakinys.didziosiomis())
print(mano_sakinys.atspausdinti_zodi(1))
print(mano_sakinys.simb_raid("i"))
print(mano_sakinys.pakeisti("diena", "vakara"))
mano_sakinys.info()
print(mano_sakinys)


