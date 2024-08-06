#ivan araluce nava A00949193
#programa para calcular la suma de numeros dados por el usuario
#08/02/2016

suma=0
contador=0
num=int(input("numero:"))

#validar que el numero no sea negativo
while(num<0):
    print("error el numero debe ser positivo")
    num=int(input("numero:"))
#solicitar los numeros
while(num>0):
    suma=suma+num
    contador=contador+1
    num=int(input("numero:"))
    #validar que el numero no sea negativo
    while(num<0):
        print("error, numero debe ser positivo")
        num=int(input("numero:"))
