fullList = []
while True:
    newNum = input("Enter a number, or press enter to end: ")
    if newNum == "":
        break
    fullList.append(float(newNum))
fullList.sort(reverse = True)
for i in range(0,5):
    print(fullList[i])