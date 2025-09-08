def listansumma(lista):
    summa = 0
    for i in lista:
        summa += i
    return summa
testList = [1,2,3,6]
print(listansumma(testList))