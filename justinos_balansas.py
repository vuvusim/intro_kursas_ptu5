import pickle

def perziura():
    try:
        with open("Naujas/uzduotispickle.pkl", 'rb') as failas:
            pajamos_islaidos = pickle.load(failas)
    except Exception as e:
        print('Failas nerastas, klaida', e)
        return []
    else:
        print('Visi biudzeto irasai: ')
        for skaicius in pajamos_islaidos:
            print(skaicius)
        return pajamos_islaidos

def irasymas(pajamos_islaidos):
    try:
        ivesta_suma = float(input('Irasykite pajamas arba islaidas su minuso zenklu: '))
        # iveskite paaiskinima
        # irasas = {"verte": ivesta_suma, "zinute": paaiskinimas}
    except ValueError:
        print('Fvestas ne skaicius')
    else:
        # appendinam irasa, kuris yra zodynas, vietoj ivestos sumos
        pajamos_islaidos.append(ivesta_suma) 
        with open("Naujas/uzduotispickle.pkl", 'wb') as failas: 
            pickle.dump(pajamos_islaidos, failas)
        return pajamos_islaidos 

pajamos_islaidos = []
while True:
    veiksmas = input('Biudzetas:\n 1 - perziureti biudzeta\n 2 - biudzeto balansas\n 3 - irasyti pajamas arba islaidas\n bet kas kitas - iseiti\nPasirinkite: ')
    if veiksmas == '1':
        pajamos_islaidos = perziura()
    elif veiksmas == '2':
        # balansui skaiciuoti reikia naujos funkcijos, kuri is zodynu isrinktu skaicius, ir juos sumuotu
        print('biudzeto balansas', sum(pajamos_islaidos))
    elif veiksmas == '3':
        pajamos_islaidos = irasymas(pajamos_islaidos)
    else:
        print('Programa baigta')
        break
