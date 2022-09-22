# Parašyti programą, kuri:

#     Leistų vartotojui įvesti skaičių.
#     Jei įvestas skaičius yra teigiamas, paprašyti įvesti dar vieną skaičių
#     Jei įvestas skaičius neigiamas, nutraukti programą ir atspausdinti visų įvestų teigiamų skaičių sumą

# Patarimas: Naudoti ciklą while, sąlygą if, break


# skaiciai = [a]


skaiciai = []

while True:
    skaicius = int(input("iveskite skaiciu: "))
    if skaicius < 0:
        break
    skaiciai.append(skaicius)
print(sum(skaiciai))

    # print(input("Iveskite skaiciu:\n"))
# for skaicius in skaiciai:
#     print("prie ", suma, "pridedam", skaicius)
#     suma += skaicius
# print("suma:", suma)


