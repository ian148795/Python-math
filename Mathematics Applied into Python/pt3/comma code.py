def commaCode(lista):
    n=" "
    for elemento in lista:
        n=n+elemento+","
    return n
#pp
lista=input("elementos de lista:")
n_string=commaCode([lista])
print(n_string)
