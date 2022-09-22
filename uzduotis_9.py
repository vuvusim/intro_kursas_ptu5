# Sukurti programą, kuri:

#     Leistų vartotojui įvesti metus
#     Atspausdintų „Keliamieji metai“, jei taip yra
#     Atspausdintų „Nekeliamieji metai“, jei taip yra


metai = int(input("metai: "))
if metai % 4 == 0 and (metai % 100 != 0 or metai % 400 == 0):
    print("Keliamieji")
else:
    print("Nekeliamieji")