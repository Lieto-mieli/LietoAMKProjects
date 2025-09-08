import math
def pizzaefficiency(halkaisija, hinta):
    pintaala = (math.pi * pow(halkaisija, 2)) / 4
    efficiency = pintaala / hinta
    return efficiency
pizza1Halkaisija = input("Anna ensimmäisen pizza halkaisija: ")
pizza1Hinta = input("Anna ensimmäisen pizza hinta: ")
pizza2Halkaisija = input("Anna toisen pizza halkaisija: ")
pizza2Hinta = input("Anna toisen pizza hinta: ")
pizza1Efficiency = pizzaefficiency(pizza1Halkaisija, pizza1Hinta)
pizza2Efficiency = pizzaefficiency(pizza2Halkaisija, pizza2Hinta)
print(pizza1Efficiency)
print(pizza2Efficiency)
if pizza1Efficiency < pizza2Efficiency:
    print("pizza 2 on edullisempi")
elif pizza1Efficiency > pizza2Efficiency:
    print("pizza 1 on edullisempi")
else:
    print("pizzat ovat yhtä edullisia")