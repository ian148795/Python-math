#ivan araluce nava
#funcion area triangulo
#09/02/2016

def areaTriangulo(b, h):
    resultado = (b*h)/2
    return resultado
#programa principal
b_str=input("base:")
b=int(b_str)
h_str=input("altura:")
h=int(h_str)
area= areaTriangulo(b, h)
print("el area es:", area)


