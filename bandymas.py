# a = int(input("Iveskite skaiciu a:\n"))
# b = int(input("Iveskite skaiciu b:\n"))

# x = input("Koki matematini veiksma norite atlikti?\n")






# if x == "*":
    # print(f"Atsakymas = {a*b}")
# elif x == "/" and a > 0 or b > 0:
    # print(f"Atsakymas = {a/b}")
    # try:
        # result = a / b
    # except ZeroDivisionError:
        # result = 0
        # print(f"Atsakymas = {result}")
# elif x == "+" and a > 0 or b > 0:
    # print(f"Atsakymas = {a+b}")
    # if x == "-":
        # print(f"Atsakymas = {a-b}")
# else:
    # print("Sorry, taip gudrai nepavyks! :D")
    # exit






a = int(input("Iveskite pirma skaiciu :\n"))
b = int(input("Iveskite antra skaiciu :\n"))

x = input(f"Koki matematini veiksma norite atlikti su siais skaiciais {a} ir {b}?\n")

result = b and a / b


if x == "*":
    print(f"Atsakymas = {a*b}")
elif x == "/":
    if result == 0:
        print(f"Atsakymas = {result}")
    elif x == "/":
        print(f"Atsakymas = {a/b}")
elif x == "+":
    print(f"Atsakymas = {a+b}")
elif x == "-":
    print(f"Atsakymas = {a-b}")
else:
    print("Sorry, taip gudrai nepavyks! :D")
    exit