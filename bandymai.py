

# pirmas budas kaip dalint is nulio su if/else salyga
# print("dalybos programele")
# sk1 = int(input("iveskite skaiciu: "))
# sk2 = int(input("iveskite skaiciu: "))
# if sk2 == 0:
#     print("negalima dalint is nulio")
# else: 
#     print(sk1/sk2)

# antras budas kaip dalint is nulio su try/except/else salyga
print("dalybos programele")
# sk1 = int(input("iveskite skaiciu: "))
# sk2 = int(input("iveskite skaiciu: "))
try:
    sk1 = int(input("iveskite skaiciu: "))
    sk2 = int(input("iveskite skaiciu: "))
    atsakymas = sk1/sk2
except ValueError:
    print("ivestas ne sakicius")
except ZeroDivisionError:
    print("negalima dalinti is nulio")
else: 
    print(atsakymas)
finally:
    print("programa vis dar veikia!!")

    