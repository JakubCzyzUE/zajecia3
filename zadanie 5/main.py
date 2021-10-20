
def funtion(i: int, lista: list):
    for x in lista:
        if i in lista:
            print("Element jest w liście")
            break
        else:
            print("Elementu nie ma w liście")
            break

lista = [10,1,23,45]
funtion(10,lista)
funtion(11,lista)