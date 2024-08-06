#ivan araluce nava a00949193
#desviacion estandar
#26/04/2016

def media(x):
    suma=0
    for numero in x:
        suma=suma+numero
    promedio=suma/len(x)
    return promedio

def desviacion(x):
    import math
    promedio=media(x)
    suma2=0
    for numero in x:
        suma2=suma2+(numero-promedio)**2
    desviacion_estandar=math.sqrt(suma2/len(x))
    return desviacion_estandar

def main():
    print(desviacion([42]))
    print(desviacion([10, 20]))
    print(desviacion([1, 2, 3, 4, 5]))
    print(desviacion([7, 7, 7, 7, 7, 7, 7]))
    print(desviacion([32, 88, 20, 26, 14, 24, 26, 44, 14, 94, 94, 72, 
                     8, 46, 92, 50, 38, 56, 60, 84]))
