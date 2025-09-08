def muunto(gallonit):
    return gallonit * 3.785
while True:
    g = float(input("Anna galloni määrä: "))
    if g >= 0:
        print(f"{muunto(g)} litraa")
    else:
        break