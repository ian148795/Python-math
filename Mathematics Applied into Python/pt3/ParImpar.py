def par(x):
    residuo=x%2
    if(residuo==0):
        return True
    else:
        return False

#programa principal
inicio = int(input("valor inicial"))
fin = int(input("valor final"))
for i in range(inicio, fin+1):
    if par(i):
        print(i, "Par")
    else:
        print(i,"impar")
