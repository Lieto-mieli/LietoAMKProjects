vuosi = int(input("anna vuosi:"))
if int(vuosi / 100)==0:
    if int(vuosi / 400) == 0:
        (
            print("vuotesi on karkausvuosi")
        )
    else:
        (
            print("vuotesi ei ole karkausvuosi")
        )
else:
    if int(vuosi / 4) == 0:
        (
            print("vuotesi on karkausvuosi")
        )
    else:
        (
            print("vuotesi ei ole karkausvuosi")
        )
#correction