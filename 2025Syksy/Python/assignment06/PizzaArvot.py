import math
def pizzaefficiency(halkaisija, hinta):
    halkaisijameters = halkaisija / 100
    pintaala = (math.pi * (pow(halkaisijameters, 2))) / 4
    efficiency = hinta / pintaala
    return efficiency
pizza1Halkaisija = float(input("Enter the diameter of the first pizza (cm): "))
pizza1Hinta = float(input("Enter the price of the first pizza (euros): "))
pizza2Halkaisija = float(input("Enter the diameter of the second pizza (cm): "))
pizza2Hinta = float(input("Enter the price of the second pizza (euros): "))
pizza1Efficiency = pizzaefficiency(pizza1Halkaisija, pizza1Hinta)
pizza2Efficiency = pizzaefficiency(pizza2Halkaisija, pizza2Hinta)
print(pizza1Efficiency)
print(pizza2Efficiency)
if pizza1Efficiency > pizza2Efficiency:
    print("The second pizza provides better value for money.")
elif pizza1Efficiency < pizza2Efficiency:
    print("The first pizza provides better value for money.")
else:
    print("pizzat ovat yhtä edullisia")