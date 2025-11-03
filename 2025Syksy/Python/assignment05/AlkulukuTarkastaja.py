num = int(input("Syötä kokonaisluku: "))
jaolliset = []
onAlkuluku = True
for i in range(2,num):
    if num%i == 0:
        onAlkuluku = False
        jaolliset.append(i)
if onAlkuluku:
    print(f"{num} on alkuluku.")
else:
    print(f"{num} ei ole alkuluku, koska se on jaollinen luvuilla:")
    for i in range(0,jaolliset.__len__()):
        print(jaolliset[i])