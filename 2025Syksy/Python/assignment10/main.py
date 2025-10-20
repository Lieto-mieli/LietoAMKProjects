class Hissi:
    def __init__(self, ylin, alin):
        self.alinKerros = ylin
        self.ylinKerros = alin
        self.kerros = alin
    def kerrosYlos(self):
        self.kerros += 1
    def kerrosAlas(self):
        self.kerros += -1
    def siirryKerrokseen(self, kerrokseen):
        while True:
            if self.kerros < kerrokseen:
                self.kerrosYlos()
                print(f"Hissi on nyt kerroksessa {self.kerros}")
            elif self.kerros > kerrokseen:
                self.kerrosAlas()
                print(f"Hissi on nyt kerroksessa {self.kerros}")
            else:
                break
class Talo:
    def __init__(self, ylin, alin, hissiMaara):
        self.hissit = []
        self.alinKerros = ylin
        self.ylinKerros = alin
        for i in range(0,hissiMaara):
            h = Hissi(ylin, alin)
            self.hissit.append(h)
    def ajaHissia(self, hissiNum, kerrokseen):
        self.hissit[hissiNum-1].siirryKerrokseen(kerrokseen)
    def palohalytys(self):
        for o in self.hissit:
            o.siirryKerrokseen(1)

t = Talo(7, 1, 2)