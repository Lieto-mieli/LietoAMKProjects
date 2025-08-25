suku = input("mikä on biologinen sukupuolesi?:")
glob = int(input("mikä on hemoglobiini arvosi? (g/l):"))
if suku.lower()=="mies":
    if glob < 134:(
        print("hemoglobiinisi on alhainen")
        )
    elif 134 < glob < 195:(
        print("hemoglobiinisi on normaali")
        )
    elif glob > 195:(
        print("hemoglobiinisi on ylhäällä")
        )
elif suku.lower()=="nainen":
    if glob < 117:(
        print("hemoglobiinisi on alhainen")
        )
    elif 117 < glob < 175:(
        print("hemoglobiinisi on normaali")
        )
    elif glob > 175:(
        print("hemoglobiinisi on ylhäällä")
        )
else:
    print("sori kamu, mut tää tehtävä ei usko intersex ihmisiin :(")