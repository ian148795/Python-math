#ivan araluce nava A00949193
#cantidad de numeros, menor y mayor
#15/03/2016

numeros=int(input("cantidad de numeros:"))
mayor=-100000
menor=100000

for i in range(1,numeros+1):
    num=int(input("numero"+ str(i)+":"))
    if(num<menor):
        menor=num
    if(num>mayor):
        mayor=num
print("El numero menor es:", menor)
print("el numero mayor es:", mayor)
