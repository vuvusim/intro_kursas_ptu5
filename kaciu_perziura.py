import pickle
from katinynas import Kate




with open("Naujas/kates.pkl", "rb") as failas:
    kates = pickle.load(failas)

for kate in kates:
    print(kate)
    # kate.miaukseti()