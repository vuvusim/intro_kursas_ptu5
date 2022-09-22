# Sukurti programą, kuri:

#     Kompiuterio darbalaukyje (Desktop) sukurtų katalogą „Naujas Katalogas“
#     Šiame kataloge sukurtų tekstinį failą, kuriame būtų šiandienos data ir laikas
#     Atspausdintų šio tekstinio failo sukūrimo datą ir dydį baitais

# Patarimai:

#     Failo sukūrimo datą galima pasiekti per os.stat(„Failas.txt“).st_ctime


from datetime import datetime
import os

try:
    os.chdir("C:\\Users\\simas\\OneDrive\\Stalinis kompiuteris\\Naujas_katalogas")
    os.mkdir("Naujas_katalogas")
except:
    "Toks folderis jau yra"


os.chdir("C:\\Users\\simas\\OneDrive\\Stalinis kompiuteris\\Naujas_katalogas")

with open("data.txt", "w") as failas:
    failas.write(str(datetime.today()))

os.chdir("C:\\Users\\simas\\OneDrive\\Stalinis kompiuteris\\Naujas_katalogas")

print("Sukurimo data", datetime.fromtimestamp(os.stat("data.txt").st_ctime))
print("Failo dydis", os.stat("data.txt").st_size)










