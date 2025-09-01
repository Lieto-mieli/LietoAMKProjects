import random
count = int(input("Kuinka monta arpakuutiota heitetään?: "))
sumOfDice = 0
for i in range(count):
    sumOfDice += random.randint(1,6)
print(sumOfDice)