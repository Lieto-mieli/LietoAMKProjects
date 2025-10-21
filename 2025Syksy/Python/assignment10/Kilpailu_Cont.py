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

class Kilpailu:
    def __init__(self, name, length_km, participants_list):
        self.name = name
        self.length = length_km
        self.cars = participants_list
        self.hour = 0
    def tunti_kuluu(self):
        for o in self.cars:
            o.kiihdyta(random.randint(-10, 15))
            o.kulje(1)
        self.hour += 1
    def tulosta_tilanne(self):
        print("")
        print(f"Contestant stats at Day {1+(self.hour//24)}, {self.hour%24}00 Hours: ")
        for o in self.cars:
            print(f"{o.rekisteriTunnus}'s results:  Max Speed: {o.huippuNopeus} km/h | Current speed: {o.nopeus} km/h | Distance travelled: {o.kuljettuMatka} km")
    def kilpailu_ohi(self):
        finish = False
        for o in self.cars:
            if o.kuljettuMatka >= self.length:
                finish = True
        if finish:
            return True
        return False
ralliAutot = []
for i in range(1,11):
    new = Auto(f"ABC-{i}", random.randint(100, 200))
    ralliAutot.append(new)
suuriRomuralli = Kilpailu("Suuri Romuralli", 8000, ralliAutot)
while True:
    suuriRomuralli.tunti_kuluu()
    if suuriRomuralli.kilpailu_ohi():
        break
    if suuriRomuralli.hour % 10 == 0:
        suuriRomuralli.tulosta_tilanne()
print("Kilpailu on ohi")
for o in suuriRomuralli.cars:
    print(f"{o.rekisteriTunnus}'s results:  Max Speed: {o.huippuNopeus} km/h | Speed at finish: {o.nopeus} km/h | Distance travelled: {o.kuljettuMatka} km")

# finish = False
# while True:
#     for o in ralliAutot:
#         o.kiihdyta(random.randint(-10,15))
#         o.kulje(1)
#         if o.kuljettuMatka >= 10000:
#             finish = True
#     if finish:
#         break
# for o in ralliAutot:
#     print(f"{o.rekisteriTunnus}'s results:  Max Speed: {o.huippuNopeus} km/h | Speed at finish: {o.nopeus} km/h | Distance travelled: {o.kuljettuMatka} km")
