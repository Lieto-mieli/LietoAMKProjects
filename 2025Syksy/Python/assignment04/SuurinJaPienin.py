suurin = 0
pienin = 0
while True:
    num = input("anna numero: ")
    if num == "":
        break
    num = float(num)
    if num<pienin:
        pienin = num
    if num>suurin:
        suurin = num
print(f"numeroista suurin oli {suurin}, ja pienin oli {pienin}")