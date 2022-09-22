# zodziai = "The Zen of Python"
# zodis = zodziai.split()
# print(zodis)

# zodis_su = "! ".join([elementas for elementas in zodis if type(elementas) is str])
# print(zodis_su)

# sakinys = map(lambda x: x + "!", zodziai.split())
# print(" ".join(sakinys))

# sakinys2 = [x + "!" for x in zodziai.split()]
# print(" ".join(sakinys2))


# Sukurti programą, kuri:

#     Sukurtų sąrašą iš skaičių nuo 0 iki 50
#     Padaugintų visus sąrašo skaičius iš 10 ir atspausdintų
#     Atrinktų iš sąrašo skaičius, kurie dalinasi iš 7 ir atspausdintų
#     Pakeltų visus sąrašo skaičius kvadratu ir atspausdintų
#     Su kvadratų sąrašu atliktų šiuos veiksmus: atspausdintų sumą, mažiausią ir didžiausią skaičių, vidurkį, medianą
#     Surūšiuotų ir atspausdintų kvadratų sąrašą atbulai

# Patarimai:

#     Naudoti map, filter arba comprehension, sum, min, max, mean, median, %
#     from statistics import mean, median
# from statistics import mean, median

# sarasas = range(0, 51)

# padauginta = list(map(lambda x: x * 10, sarasas))
# print(padauginta)

# dalinasi_is_7 = list(filter(lambda x: x % 7 == 0, sarasas))
# print(dalinasi_is_7)

# kvadratu = list(map(lambda x: x ** 2, sarasas))
# print(kvadratu)

# print("Suma: ", sum(kvadratu))
# print("Min: ", min(kvadratu))
# print("Max: ", max(kvadratu))
# print("Vidurkis: ", mean(kvadratu))
# print("Median: ", median(kvadratu))

# surusiuotas = sorted(kvadratu)
# atbulai = surusiuotas[::-1]
# print(atbulai)



# Duotas sąrašas: sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

# Sukurti programą, kuri:

#     Paskaičiuotų ir atspausdintų visų sąrašo skaičių sumą
#     Sudėtų ir atspausdintų visus sąrašo žodžius
#     Suskaičiuotų ir atspausdintų, kiek sąraše yra loginių (boolean) kintamųjų su True reikšme

# Patarimai:

#     Naudoti filter arba comprehension, sum, " ".join()


sarasas = [2.5, 2, "Labas", True, False, 5, 7, 8, 2.8, "Vakaras"]

suma = sum(type(elem) in (int, float) for elem in sarasas)
print(suma) # kaip atrinktus skaicius sudeti 

zodziai = " ".join([x for x in sarasas if type(x) is str])
print(zodziai)

bol = len([x for x in sarasas if type(x) is bool]) 
print(bol) # kaip atspausdintu kad istikruju True o ne False



# Sukurti programą, kuri:

#     Turėtų klasę Zmogus, su savybėmis vardas ir amzius
#     Klasėje būtų repr metodas, kuris atvaizduotų vardą ir amžių
#     Inicijuoti kelis Zmogus objektus su vardais ir amžiais
#     Įdėti sukurtus Zmogus objektus į naują sąrašą
#     Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą ir pagal amžių (ir atbulai)

# Patarimai:

#     Naudoti sorted, attrgetter, reverse, funkciją repr
#     from operator import attrgetter

# from operator import attrgetter 

# class Zmogus():
#     def __init__(self, vardas, amzius):
#         self.vardas = vardas
#         self.amzius = amzius

#     def __repr__(self):
#         return f"{self.vardas} {self.amzius}"

# z1 = Zmogus("Arturas", 35)
# z2 = Zmogus("Simas", 28)
# z3 = Zmogus("Bicas", 45)

# zmones = [z1, z2, z3]

# def pagal_varda(zmogus):
#     return zmogus.vardas

# def pagal_amziu(zmogus):
#     return zmogus.amzius


# rusiavimas1 = sorted(zmones, key=pagal_varda)
# rusiavimas2 = sorted(zmones, key=pagal_amziu)
# rusiavimas3 = sorted(zmones, key=attrgetter("vardas"), reverse=True)


# print(f"Rusiavimas pagal varda: {rusiavimas1} \nRusiavimas pagal amziu: {rusiavimas2}")
# print(f"Rusiavimas nuo galo: {rusiavimas3}")



