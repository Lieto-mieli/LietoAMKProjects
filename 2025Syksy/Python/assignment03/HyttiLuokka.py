hyttiLuokka = input("Mikä on laivan hyttiluokka?:")
if hyttiLuokka.upper()=="LUX":
    (
        print("LUX on parvekkeellinen hytti yläkannella.")
    )
elif hyttiLuokka.upper()=="A":
    (
        print("A on ikkunallinen hytti autokannen yläpuolella.")
    )
elif hyttiLuokka.upper()=="B":
    (
        print("B on ikkunaton hytti autokannen yläpuolella.")
    )
elif hyttiLuokka.upper()=="C":
    (
        print("C on ikkunaton hytti autokannen alapuolella.")
    )
else:
    (
        print("Virheellinen hyttiluokka")
    )