ivestas = int(input("Iveskite sakiciu: "))
for skaicius in range(1, ivestas+1):
    print(skaicius)
    if skaicius == 5:
        print("nutrauktas ciklas")
        break
else:
    print("ciklas nebuvo nutraukas")
