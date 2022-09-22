# while True:
#     try:
#         skaicius = float(input("iveskite skaiciu: "))
#     except ValueError:
#         print("bandykite dar")
#     else:
#         break




from datetime import date, time, datetime, timedelta


while True:
    datairlaikas = input("iveskite norima data ir laika YYYY-MM-DD HH:MM:SS formatu: ")
    try:
        suformatuotas_laikas = datetime.strptime(datairlaikas, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("blogas formatas")
    else:
        skirtumas = datetime.now() - suformatuotas_laikas
        metai = skirtumas.days // 365
        menesiai = int(skirtumas.days / 365 * 12 - metai * 12)
        dienos = int(skirtumas.days - metai * 365 - menesiai * 30.4)
        valandos = int(skirtumas.seconds // 60 // 60)
        minutes = int(skirtumas.seconds // 60 - valandos * 60)
        sekundes = int(skirtumas.seconds - valandos * 60 * 60 - minutes * 60)
        print(f"Nuo jusu parasyto laiko praejo: {metai} metai")
        print(f"Nuo jusu parasyto laiko praejo: {menesiai} menesiai")
        print(f"Nuo jusu parasyto laiko praejo: {dienos} dienos")
        print(f"Nuo jusu parasyto laiko praejo: {valandos}valandos/u")
        print(f"Nuo jusu parasyto laiko praejo: {minutes}minutes/ciu")
        print(f"Nuo jusu parasyto laiko praejo: {sekundes}sekundes/dziu")
        break
