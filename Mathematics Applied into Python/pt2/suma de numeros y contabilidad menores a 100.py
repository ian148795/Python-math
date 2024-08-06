suma=0
cont=0
num=int(input("inserte un numero:"))
while(num!=0):
    suma=suma+num
    if(num<100):
        cont=cont+1
    num=int(input("inserte un numero:"))
print("la suma es:", suma)
print("la cantidad de numeros menores a 100 son:",cont)
