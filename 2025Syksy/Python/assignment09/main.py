import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteriTunnus = rekisteritunnus
        self.huippuNopeus = huippunopeus
        self.nopeus = 0
        self.kuljettuMatka = 0
    def kiihdyta(self, nopeudenmuutos_kmh):
        self.nopeus += nopeudenmuutos_kmh
        self.nopeus = min(self.nopeus, self.huippuNopeus)
        self.nopeus = max(self.nopeus, 0)
    def kulje(self, matka_h):
        self.kuljettuMatka += matka_h*self.nopeus
    def race(self):
        return
ralliAutot = []
for i in range(1,11):
    new = Auto(f"ABC-{i}", random.randint(100, 200))
    ralliAutot.append(new)
finish = False
while True:
    for o in ralliAutot:
        o.kiihdyta(random.randint(-10,15))
        o.kulje(1)
        if o.kuljettuMatka >= 10000:
            finish = True
    if finish:
        break
for o in ralliAutot:
    print(f"{o.rekisteriTunnus}'s results:  Max Speed: {o.huippuNopeus} km/h | Speed at finish: {o.nopeus} km/h | Distance travelled: {o.kuljettuMatka} km")
# cool = Auto("asda", 120)
# print(f"{cool.rekisteriTunnus} {cool.huippuNopeus} {cool.nopeus} {cool.kuljettuMatka}")
# cool.kiihdyta(30)
# cool.kiihdyta(70)
# cool.kiihdyta(50)
# print(f"auton nopeus on {cool.nopeus} km/h")
# cool.kiihdyta(-200)
# print(f"auton nopeus on {cool.nopeus} km/h")
