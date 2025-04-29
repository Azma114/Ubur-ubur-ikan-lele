import random

class petarung:
    def __init__(self,nama):
        self.nama = nama
        self.kesehatan = 100
        self.kekuatan = random.randint(0,100)
        self.kecerdasan = random.randint(0,100)
        self.kelincahan = random.randint(0,100)
        self.senjata = random.randint(0,100)

    def print_data(self):
        print(self.nama)
        print("kesehatan = ", self.kesehatan)
        print("kekuatan = ", self.kekuatan)
        print("kecerdasan = ", self.kecerdasan)
        print("kelincahan = ", self.kelincahan)
        print("senjata = ", self.senjata)

Nobita = petarung("Nobita")
Giant = petarung("Giant")
Nobita.print_data()
print("----------------------")
Giant.print_data()
