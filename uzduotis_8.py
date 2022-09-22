# Kauliukų žaidimas

# Sukurti programą, kuri:

#     Sugeneruotų tris atsitiktinius skaičius nuo 1 iki 6
#     Jei vienas iš šių skaičių yra 5, atspausdinti „Pralaimėjai...“
#     Kitu atveju atspausdinti „Laimėjai!“

# Patarimas: Naudoti while ciklą, funkciją random.randint (import random), else, break

import random

for eiles_nr in range(3):
    atsitiktiniai = random.randint(1,6)
    print(f"Atsitiktinis {eiles_nr+1} skaicius: ", atsitiktiniai)
    if atsitiktiniai == 5:
        print("Pralaimejai...")
        break
else:
    print("Laimejai!")