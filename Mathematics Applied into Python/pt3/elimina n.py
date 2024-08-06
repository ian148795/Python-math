def elimina(lista, n):
    lista2=[]
    for x in lista:
        if x!=n:
            lista2.append(x)
    return lista2

print(elimina([1,5,4,2,1],1))
