a = int(input("Iveskite pirma skaiciu :\n"))
b = int(input("Iveskite antra skaiciu :\n"))

x = input(f"Koki matematini veiksma norite atlikti su siais skaiciais {a} ir {b}?\n")

result = b and a / b


if x == "*":
    print(f"Atsakymas = {a*b}")
elif x == "/":
    if result == 0:
        print(f"Toks atsakymas negalimas.")
    elif x == "/":
        print(f"Atsakymas = {a/b}")
elif x == "+":
    print(f"Atsakymas = {a+b}")
elif x == "-":
    print(f"Atsakymas = {a-b}")
else:
    print("Sorry, taip gudrai nepavyks! :D")
    exit





# a = int(input("Iveskite skaiciu a:\n"))
# b = int(input("Iveskite skaiciu b:\n"))
# 
# x = input("Koki matematini veiksma norite atlikti?\n")
# 
# 
# if x == "*":
    # print(a*b)
# elif x == "/":
    # print(a/b)
# elif x == "+":
    # print(a+b)
# elif x == "-":
    # print(a-b)
# else:
    # print("Sorry, taip gudrai nepavyks! :D")
    # exit


# else:
    # print(float(a/b))
# else x == "+":
    # print(a+b)
# else x == "-":
    # print(a-b)
# else:
    # print("Sorry, taip gudrai nepavyks! :D")
    # exit



# a = 0
# b = 0






