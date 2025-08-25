name = "python"
password = "rules"
while True:
    givenName = input("Enter username: ")
    givenPassword = input("Enter password: ")
    if givenName==name and givenPassword==password:
        break
    else:
        print("Pääsy evätty")
print("Tervetuloa")