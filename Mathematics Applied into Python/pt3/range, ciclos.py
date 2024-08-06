#1 Powers
for i in range(1,11):
    print(i,2**i)


#2 Table
import math 
for i in range(10,60,10):
    print(i, math.log (i), i*math.log (i), i**2, 2**i)

#3 Temptable

def fahrenheit_celsius(f):
    c=(5/9)*(f-32)
    return c
for f in range(-30,80,10):
    c=fahrenheit_celsius(f)
    print(f, "°f =",c, "°c")

#4 distable

def miles_to_km(m):
    km = m*1.609
    return km
for m in range(100,1100,100):
    km=miles_to_km(m)
    print(m, "miles =" ,km, "km")

#5 Pyramid
def pyramid(n):
    suma = n**2
    return suma
#programa principal
cont=0
for i in range(1,16):
    suma = pyramid (i)
    cont+=suma
    print(i, cont)










    

    
    
