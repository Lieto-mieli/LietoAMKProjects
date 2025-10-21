class Hissi:
    def __init__(self, ylin, alin):
        self.ylinKerros = ylin
        self.alinKerros = alin
        self.kerros = alin
    def kerros_ylos(self):
        if self.kerros+1 <= self.ylinKerros:
            self.kerros += 1
            return True
        else:
            return False
    def kerros_alas(self):
        if self.kerros - 1 >= self.alinKerros:
            self.kerros += -1
            return True
        else:
            return False
    def siirry_kerrokseen(self, kerrokseen):
        while True:
            if self.kerros < kerrokseen:
                if self.kerros_ylos():
                    print(f"Hissi on nyt kerroksessa {self.kerros}")
                else:
                    break
            elif self.kerros > kerrokseen:
                if self.kerros_alas():
                    print(f"Hissi on nyt kerroksessa {self.kerros}")
                else:
                    break
            else:
                break
class Talo:
    def __init__(self, ylin, alin, hissiMaara):
        self.hissit = []
        self.ylinKerros = ylin
        self.alinKerros = alin
        for i in range(1,hissiMaara+1):
            newh = Hissi(ylin, alin)
            self.hissit.append(newh)
    def aja_hissia(self, hissiNum, kerrokseen):
        self.hissit[hissiNum-1].siirry_kerrokseen(kerrokseen)
    def palohalytys(self):
        for o in self.hissit:
            o.siirry_kerrokseen(self.alinKerros)

h = Hissi(5, 1)
h.siirry_kerrokseen(4)
h.siirry_kerrokseen(-999)

t = Talo(7, 1, 2)
t.aja_hissia(1, 6)
t.aja_hissia(2, 3)
t.palohalytys()