# Sukurti programą, kuri:

#     Leistų vartotojui po vieną įvesti 5 žodžius
#     Pridėtų įvestus žodžius į sąrašą
#     Atspausdintų kiekvieną žodį, jo ilgį ir eilės numerį sąraše (nuo 1)

# Sudėtingiau: kad programa leistų įvesti norimą žodžių kiekį

# Patarimas: Naudoti sąrašą (list), ciklą for, funkcijas len ir index

ivesti = []
zodziu_kiekis = int(input("Kiek zodziu?: "))
for eiles_nr in range(zodziu_kiekis):
    ivesti.append(input(f"Iveskite {eiles_nr+1} zodi: "))

for indexas, elementas in enumerate(ivesti):
    print(indexas+1, elementas, len(elementas))



