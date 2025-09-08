lentoasemat = {}
while True:
    ans = input("Haluatko lisätä uuden lentoaseman (1), hakea lentoaseman tiedot (2), vai lopettaa ohjelman (3)")
    if ans == 1:
        ICAO = input("Mikä on uuden lentoaseman ICAO koodi?: ")
        nimi = input("Mikä on uuden lentoaseman nimi?: ")
        lentoasemat[ICAO] = nimi
    elif ans == 2:
        query = input("Mikä on lentoaseman ICAO koodi?: ")
        print(f"Lentoaseman nimi on {lentoasemat[query]}")
    else:
        break