import random
def noppa(tahko):
    return random.randint(1,tahko)
tahkot = int(input("Kuinka moni-tahkoista noppaa heitetään?: "))
while True:
    tulos = noppa(tahkot)
    print(tulos)
    if tulos == tahkot:
        break