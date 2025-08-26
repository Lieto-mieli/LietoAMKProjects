vuosi = int(input("anna vuosi:"))
if int(vuosi / 100) == vuosi / 100:
    if int(vuosi / 400) == vuosi / 400:
        (
            print("vuotesi on karkausvuosi")
        )
    else:
        (
            print("vuotesi ei ole karkausvuosi")
        )
elif int(vuosi / 4) == vuosi / 4:
    (
        print("vuotesi on karkausvuosi")
    )
else:
    (
        print("vuotesi ei ole karkausvuosi")
    )