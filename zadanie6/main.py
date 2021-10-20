
def funtion(listA: list, listB: list)->list:
    listA2 = []
    for x in listA:
        listA2.append(x**3)
    print(listA2)

    listB2 = []
    for x in listB:
        listB2.append(x**3)
    print(listB2)

    listC = listA2 + listB2
    print(listC)
    return listC


lista1 = [1,2,3,4,5]
lista2 = [10,293,112]

funtion(lista1, lista2)