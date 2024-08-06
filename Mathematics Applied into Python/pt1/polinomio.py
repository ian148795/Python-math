#ivan araluce nava A00949193
#20/01/2016
#polinomio
import math
print("teclea los valores de las siguientes letras:")
a=int(input("teclea el valor de a:"))
b=int(input("teclea el valor de b:"))
c=int(input("teclea el valor de c:"))

x1= (-b+ math.sqrt(b**2-4*a*c))/(2*a)
x2= (-b- math.sqrt(b**2-4*a*c))/(2*a)
print("los valores del polinomio son:", x1, x2)

