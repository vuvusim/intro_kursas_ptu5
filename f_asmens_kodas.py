lytis_LT = input("Įveskite savo lytį (M - moteris, V - vyras): ")
lytis = lytis_LT.casefold()
gim_data = input("Įveskite savo gimimo metus (YYYY/MM/DD): ")
eil_nr = input("Įveskite, kelintas iš eilės gimęs kūdikis (XXX): ")
# Įvestą datą suskaldom į metus, mėnesius ir dienas
gim_metai = int(gim_data[:4])
gim_menuo = gim_data[5:7]
gim_diena = gim_data[8:]

# Nustatome, kuriame amžiuje žmogus yra gimęs
def f_amzius ():
    amzius = 0
    if 800 <= (gim_metai - 1000) < 900:
        amzius = gim_metai // 100 + 1 # pridedame 1, kad gautusi 19 amžius 1864/100=18,64+1=19
    elif (900 <= (gim_metai - 1000) < 1000):
        amzius = gim_metai // 100 + 1
    else:
        amzius = gim_metai // 100 + 1
    return amzius

# lyties nustatymas
a = 0
if lytis == "m" and f_amzius() == 20:
    a = 4
elif lytis == "m" and f_amzius() == 21:
    a = 6
elif lytis == "m" and f_amzius() == 19:
    a = 2
elif lytis == "v" and f_amzius() == 20:
    a = 3
elif lytis == "v" and f_amzius() == 21:
    a = 5
else:
    a = 1

#print (f"Žmogus yra gimęs {f_amzius()} amžiuje, yra {lytis}, pirmoji kodo A reikšmė yra {a}")
b = int(gim_data[2])
c = int(gim_data[3])
d = int(gim_menuo[0])
e = int(gim_menuo[1])
f = int(gim_diena[0])
g = int(gim_diena[1])
# Išskaidom gimusiu kūdikių skaičių dalimis
h = int(eil_nr[0])
i = int(eil_nr[1])
j = int(eil_nr[2])

s = a*1 + b*2 + c*3 + d*4 + e*5 + f*6 + g*7 + h*8 + i*9 + j*1
s2 = a*3 + b*4 + c*5 + d*6 + e*7 +f*8 + g*9 + h*1 + i*2 + j*3
if s % 11 != 10:
    k = s % 11
elif s2 % 11 !=10:
    k = s2 % 11
else:
    k = 0
print(f"Jūsų asmens kodas yra: ")
print(a,b,c,d,e,f,g,h,i,j,k)