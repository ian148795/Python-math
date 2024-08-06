import numpy as np
import matplotlib.pyplot as plt
a = np.zeros(5)
for i in range (0,5):
    a[i]=int(input("coeficiente"+str(i)+":"))
x=int(input("valor de x:"))
t=np.zeros(5)
t[0]=a[0]
for k in range(0,5):
    t[k]=t[k-1]*x+a[k]
print ("el valor de x es:",x,"es:",t[4])
