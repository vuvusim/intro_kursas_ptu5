metu_input = int(input("iveskite metus: "))

if metu_input % 4 == 0:
    if metu_input % 100 == 0:
        if metu_input % 400 == 0:
            print("Keliamieji metai")
        else:
            print("Ne")
    else:
        print("Keliamieji")
else:
    print("Ne")