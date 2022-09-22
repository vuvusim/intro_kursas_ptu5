
import pickle
import datetime


def perziura():
    try:
        with open("Naujas/zmones.pkl", "rb") as failas:
            zmones = pickle.load(failas)
    except Exception as e:
        print("Nepavyko nuskaityti failo, klaida:", e)
        return []
    else:
        for zmogus in zmones:
            print(zmogus)
        return zmones


def irasymas(zmones):

    # ivedame naujo zmogaus varda
    vardas = input("iveskite naujo zmogaus varda: ")

    # pridedame nauja varda i sarasa
    zmones.append(vardas)

    # isaugome atnaujinta sarasa i pickle faila
    with open("Naujas/zmones.pkl", "wb") as failas:
        pickle.dump(zmones, failas)

    #grazinam atnaujinta sarasa
    return zmones


# programeles karkasas
zmones = []
while True:
    veiksmas = input("Zmoniu katalogas:\n 1 - perziureti\n 2 - irasyti\n betkas kitas - iseiti\nPasirinkite veiksma:")
    if veiksmas == "1":
        zmones = perziura()
    elif veiksmas == "2":
        zmones = irasymas(zmones)
    else:
        print("programa baigta!")
        break





























