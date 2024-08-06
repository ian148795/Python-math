def cuadradoLista(lista):
    listacuadrados=[]
    for x in lista:
        listacuadrados.append(x**2)
    return listacuadrados
print(cuadradoLista([1,10,100,1000]))
