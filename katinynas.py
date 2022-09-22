# parasyti veikiancia programa katinynui:
# - sukurti klase kate, kuri turetu atributus kates vardui, spalvai, amziui ir koju kiekiui
# - kate turi sugebeti miaukseti ir begti, judinant kojasir ziureti kur bega
# - senstant kates pradeda eiti o pasenus - tik sliauzti
# - programa turi leisti ivesti kate
# - esant bent vienai katei, programa turi leisti parodyti kaciu sarasa
# - esant bent vienai katei programa turi leisti pavedzioti pasirinkta kate 
# - kate turi begti ir miaukseti tiek kartu kiek yra metu
# - issaugoti katinyno kataloga pickle faile
import pickle


class Kate():
    def __init__(self, vardas, spalva="juoda", amzius=0, kojos=4): # self kreipiasi i objekta kuris buna sukurtas klases  ## () lemia eiliskumas
        self.vardas = vardas
        self.spalva = spalva
        self.amzius = amzius
        self.kojos = kojos # jei nori keisti objekto reiksmes parametru 
        

    def __str__(self):
        return f"{self.vardas}, {self.amzius} metu, {self.kojos}-kojis, spalva: {self.spalva}" 

    def _judinti_kojas(self):
        pass

    def _ziureti_kur_begi(self):
        pass

    def miaukseti(self, zinute="miau ", kartai=1):
        print(zinute * kartai)

    def begti(self):
        self._judinti_kojas()
        self._ziureti_kur_begi()
        if self.amzius > 15:
            print("sliauziu")
        elif self.amzius > 12:
            print("einu")
        else:
            print("begu")


def ivesti():
    vardas = input("Vardas: ")
    spalva = input("Spalva (juodas): ")
    if not len(spalva):
        spalva = "juodas"
    try:
        amzius = int(input("Amzius: "))
    except ValueError:
        amzius = 0
    try:
        kojos = int(input("Kojos (4): "))  
    except ValueError:
        kojos = 4
    nauja_kate = Kate(vardas, spalva, amzius, kojos)
    return nauja_kate # galima tiesiai kviesti kates objekto sukurima


def rodyti_kataloga(kates):
    for numeris, kate in enumerate(kates):
        print(numeris+1, kate)


def vedzioti(kate):
    print(kate.vardas)
    kate.begti()
    kate.miaukseti(kartai=kate.amzius)

def issaugoti(kates):
    with open("Naujas/kates.pkl" "wb") as failas:
        pickle.dump(kates, failas)
    print(f"{len(kates)} issaugotos sekmingai!")

def atidaryti():
    with open("Naujas/kates.pkl", "rb") as failas:
        kates = pickle.load(failas)
    return kates


try:
    kates = atidaryti()
except Exception as e:
    print(e.__class__, e)
    kates = []




while True:
    print("Katinynas") # programos meniu
    print("1 - ivesti: ")
    if len(kates) > 0:
        print("2 - rodyti kataloga: ")
        print("3 - vedzioti kate: ")
        print("4 - issaugoti: ")

    
    veiksmas = input("betkas kitas - iseiti\nPasirinkite: ") # veiksmo nuskaitymas ir apdorojimas
    if veiksmas == "1":  # ivedimas
        kates.append(ivesti())


    elif len(kates) and veiksmas == "2": # katalogo rodymas
        rodyti_kataloga(kates)


    elif len(kates) and veiksmas == "3":  # vedziojimas
        try:
            numeris = int(input(f"pasirinkite kate nuo 1 iki {len(kates)+1}: "))
        except ValueError:
            print("Ivestas ne skaicius")
        else:
            if numeris >= 1 and numeris <= len(kates) +1:
                vedzioti(kates[numeris-1])
            else:
                print("Neteisingas skaicius, arba per didelis, arba per mazas")


    elif len(kates) and veiksmas == "4":
        issaugoti(kates)

        
    else:
        print("iki!")
        break