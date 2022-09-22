# Sukurti programą, kuri:

#     Sukurtų failą „Tekstas.txt“ su pilnu tekstu, gauto python kode paleidus „import this“.
#     Atspausdintų tekstą iš sukurto failo
#     Paskutinėje sukurto failo eilutėje pridėtų šiandienos datą ir laiką
#     Sunumeruotų teksto eilutes (kiekvienos pradžioje pridėtų skaičių).
#     Sukurtame faile eilutę "Beautiful is better than ugly." pakeistų į "Gražu yra geriau nei bjauru."
#     Atspausdintų visą failo tekstą atbulai
#     Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
#     Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS

# Patarimai:

#     Naudoti from datetime import datetime, datetime.today()
#     Kintamajam priskirti sakinį, kuriuo bus operuojama, eilutėmis
#     Kai kur galima panaudoti funkcijas iš praeitų pamokų

# Galima panaudoti 4 užduotyje:

# import this

#   #1
import datetime

tekstas = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

with open("Naujas/tekstas.txt", "w") as poemos_failas:
    poemos_failas.write(tekstas)


#   #2
with open("Naujas/tekstas.txt", "r") as poemos_failas:
    print(poemos_failas.read())


    

#    #4
with open("Naujas/tekstas.txt", "r") as skaitomas:
    eilutes = skaitomas.readlines()
    print(eilutes)

for indeksas, eilute in enumerate(eilutes, + 1):
    print(indeksas, eilute, end="")

#   #5
with open("Naujas/tekstas.txt", "r", encoding="UTF-8") as taisomas:
    eilutes = taisomas.readlines()
eilutes[1] = eilutes[1].replace("Beautiful is better than ugly.", "Gražu yra geriau nei bjauru.")

for eilute in eilutes:
    print(eilute, end="")
with open("Naujas/tekstas.txt", "w", encoding="UTF-8") as pataisymas:
    pataisymas.writelines(eilutes)


#   #6
print(tekstas[::-1])



#   #7
def kiek_raidziu(tekstas):
    mazos = 0
    dideles = 0
    skaiciai = 0
    zodis = 0
    for raide in tekstas:
        if raide.isupper():
            dideles += 1 
        elif raide.islower():
            mazos += 1
        elif raide.isnumeric():
            skaiciai += 1
    else:
        print(f"Zodziu kiekis:", len(tekstas.split()))
        

    print(f"Didziuju raidziu: {dideles}, mazuju raidziu: {mazos}, skaiciu: {skaiciai}")

kiek_raidziu(tekstas)




def patikrinti_sakini(tekstas):
    # Jei nori rasti zodziu kieki turi splitint teksta
    print("Žodžių kiekis:", len(tekstas.split()))

    # Jei norim surast skaiciu kieki tekste
    print("Skaičių kiekis:", sum(c.isdigit() for c in tekstas))

    # Jei norim surast didziuju raidziu kieki tekste
    print("Didžiųjų raidžių:", sum(c.isupper() for c in tekstas))

    # Jei norim surast mazuju raidziu kieki tekste
    print("Mažųjų raidžių:", sum(c.islower() for c in tekstas))


# atsidarom faila isnaujo (as failas)
with open("Naujas/tekstas.txt", "r") as failas:

    # issiprintinam funkcija (patikrinti_sakini)
    print(patikrinti_sakini(failas.read()))




#   #8
# kopijuojam faila
with open("Naujas/tekstas.txt", "r") as failas:
    with open("Naujas/tekstas_2.txt", "w") as kopija:
        while True:
            buferis = failas.read(1000)
            kopija.write(buferis.upper())
            if len(buferis) < 1000:
                break

#     #3

# pridedam data ir laika 
dabar = datetime.datetime.now()
with open("Naujas/tekstas.txt", "a") as tekstas:
    tekstas.write(str(dabar))
print(dabar)

