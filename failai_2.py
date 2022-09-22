# Sukurti programą, kuri:

#     Leistų vartotojui įvesti norimą eilučių kiekį
#     Įrašytų įvestą tekstą atskiromis eilutėmis į failą
#     Leistų vartotojui įrašyti norimą kuriamo failo pavadinimą

# Patarimai:

#     Sukurti while ciklą, kuris užsibaigtų tik įvedus vartotojui tuščią eilutę (nuspaudus ENTER)



tekstas = ""

while True:
    pirmas = input("Iveskite norima zodi arba zodzius: ")
    if pirmas != "":
        tekstas += pirmas + "\n"
    else:
        break

teksto_failas = input("Irasykite kuriamo failo pavadinima: ")

with open(teksto_failas + ".txt", "w", encoding="UTF-8") as failas:
    failas.write(tekstas)