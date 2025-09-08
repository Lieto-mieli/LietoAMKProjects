nimet = set.__new__(set)
while True:
    nimi = input("Anna nimi: ")
    if nimi == "":
        break
    elif nimet.__contains__(nimi):
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)
for i in nimet:
    print(i)