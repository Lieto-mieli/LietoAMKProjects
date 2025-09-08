def listansumma(lista):
    for i in lista:
        if i%2 != 0:
            lista.remove(i)
    return lista
testList = [1,2,3,6]
print(testList)
print(listansumma(testList))