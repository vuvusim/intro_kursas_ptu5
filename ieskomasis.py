sarasas = [25, 55, 12, 14, 88, 77, 12, 9, 8, 74, 63, 10]
ieskomasis = int(input("Iveskite skaiciu: "))
for skaicius in sarasas:
    print(skaicius, end=", ")
    if skaicius == ieskomasis:
        print("RADAU!")
        break
else:
    print("skaicius nerastas.")
print("...THE END...")