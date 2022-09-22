import datetime


ivesta_data_laikas = input("iveskite data ir laika YYYY-MM-DD HH:MM:SS formatu: ")
# strftime formatuoji datetime kintamaji i teksta
# strptime formatuoji datetime kintamaji i data ir laiak
suforrmatuotas_laikas = datetime.datetime.strptime(ivesta_data_laikas, "%Y-%m-%d %H:%M:%S")
skirtumas = datetime.datetime.now() - suforrmatuotas_laikas
print(skirtumas)