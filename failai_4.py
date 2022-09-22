# Sukurti minibiudžeto programą, kuri:

#     Leistų vartotojui įvesti pajamas arba išlaidas (su "-" ženklu)
#     Pajamas ir išlaidas saugotų sąraše, o sąrašą pickle faile (uždarius programą, įvesti duomenys nedingtų)
#     Atvaizduotų jau įvestas pajamas ir išlaidas
#     Atvaizduotų įvestų pajamų ir išlaidų balansą (sudėtų visas pajamas ir išlaidas)

# Patarimas:    
# 
import pickle

def perziura():
    try:
        with open("Naujas/biudzetas.pkl", "rb") as failas:
            biudzetas = pickle.load(failas)
    except ValueError as e:
        print("Nepavyko nuskaitytit failo, klaida:", e)
        return []
    else:
        # appendinam irasa kuris yra zodynas vietoj ivestos sumos
        for mini_biudzetas in biudzetas:
            print(mini_biudzetas)
        return biudzetas

def irasymas(biudzetas):
    pajamos_islaidos = float(input("Iveskite savo pajamas ar islaidas: "))
    # iveskite paaiskinima
    # irasas = {"verte": ivesta_suma, "zinute": paaiskinimas}
    biudzetas.append(pajamos_islaidos)
    with open("Naujas/biudzetas.pkl", "wb") as failas:
        pickle.dump(biudzetas, failas)
    return biudzetas


def sumuojam(biudzetas):
    suma = 0
    with open("Naujas/biudzetas.pkl", "rb")as failas:
        biudzetas = pickle.load(failas)

        for skaicius, irasas in enumerate(biudzetas):
            suma += irasas
            print(skaicius + 1, irasas)
        print("Biudzeto balansas", suma)
        



biudzetas = []
while True:
    veiksmas = input("Biudzetas:\n 1 - perziura\n 2 - pajamos/islaidos\n 3 - pajamu ir islaidu suma\n Betkas kita - iseiti\nPasirinkite veiksma: ")
    if veiksmas == "1":
        biudzetas = perziura()
    elif veiksmas == "2":
        # balansui skaiciuoti reikia naujos funkcijos kuri is zodynu isrinktu skaicius ir juos susumuotu
        biudzetas = irasymas(biudzetas)
    elif veiksmas == "3":
        biudzetas = sumuojam(biudzetas)

    else:
        print("Programos pabaiga")
        break




