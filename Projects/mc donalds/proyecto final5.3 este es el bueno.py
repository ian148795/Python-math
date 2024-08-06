#================================================
# Proyecto final programacion (Mcdonalds - drivethru)
#
# Descripción del proyecto: la finalidad de estro proyecto no es acabar un problema
# en si, mas bien hacer mas eficiente algo que ya esta creado que es el drivethru
# actualmente utilizado en casi todos los restaurantes del mundo. Lo que nosotros
# creamos fue un programa con el cual el cliente puede ordenar por si mismo lo que
# que quiere, esos datos se mandan a la pantalla de ordenes y se imprime un ticket
# con su pedido.

def paquete(b, a):
    pre = input('¿Deseas agrandar por 10 pesos mas?(si/no): ')
    while pre not in 'si' and pre not in 'no':
        print('Opcion no existe, intente de nuevo')
        pre = input('¿Deseas agrandar por 10 pesos mas?(si/no): ')
    if pre == 'si':
        n=a+10
    else:
        n=a
    return ([b, n])

#==========================================
# Función para la suma del total
# Entrada: una lista de números y productos
# Salida: el total de la cuenta
# Autor: Mario Martinez, Salavador Mata y la Miss
#==========================================
def sumatotal(x):
    contador = 0 
    for i in x:
        contador = i[1]+contador
    return contador

#Presentacion
titulo = "!Bienvenido a Mcdonalds(Drive thru)¡"
print(titulo.center(70, "-"))

# Abrir el menu
file1 = open('mcd.txt','r')
for line in file1:
    print(line,end='')
file1.close()

# precios
d = ['Papas', 20]
e = ['Mc.Patatas', 25]
f = ['Refresco', 20]
g = ['Cono', 10]
h = ['Mcflurry', 30]

#orden
lista = []
orden = input("¿Que desea ordenar?: ")
while orden not in 'abcdefgh':
    print('Esa opcion no existe, intenta de nuevo.')
    orden=input('¿Que deseas ordenar? ')
if orden == 'a':
    paq = paquete('Bigmac', 60)
    lista.append(paq)
elif orden == 'b':
    paq = paquete('MCPollo', 60)
    lista.append(paq)
elif orden == 'c':
    paq = paquete('Angus', 47)
    lista.append(paq)
elif orden == 'd':
    lista.append(d)
elif orden == 'e':
    lista.append(e)
elif orden == 'f':
    lista.append(f)
elif orden == 'g':
    lista.append(g)
elif orden == 'h':
    lista.append(h)
    
# Agregar algo a la orden
agreg = input("¿Desea agregar algo mas a su orden?(si/no): ")
while agreg not in('si') and agreg not in ('no'):
   print('Esa opcion no existe, intenta de nuevo') 
   agreg = input("¿Desea agregar algo mas a su orden?(si/no): ")
while agreg !='no':
    agregar = input("¿Que desea agregar?: ")
    if agregar not in 'abcdefgh':
        print('Esa opcion no existe, intenta de nuevo')
        agregar = input('¿Que desea agregar? ')
    if agregar == 'a':
        paq = paquete('Bigmac', 60)
        lista.append(paq)
    elif agregar == 'b':
        paq = paquete('MCPollo', 60)
        lista.append(paq)
    elif agregar == 'c':
        paq = paquete('Angus', 47)
        lista.append(paq) 
    elif agregar == 'd':
        lista.append(d)
    elif agregar == 'e':
        lista.append(e)
    elif agregar == 'f':
        lista.append(f)
    elif agregar == 'g':
        lista.append(g)
    elif agregar == 'h':
        lista.append(h)
    agreg = input("¿Desea agregar algo mas a su orden?(si/no): ")
    while agreg not in('si') and agreg not in ('no'):
       print('Esa opcion no existe, intenta de nuevo') 
       agreg = input("¿Desea agregar algo mas a su orden?(si/no): ")
        
#sumar lista y final
total = sumatotal(lista)

for i in lista:
    file1=open('recibo.txt','a')
    print(i[0],'.........','$',i[1],file=file1)
    print(' ',file=file1)
    file1.close()
file1=open('recibo.txt','a')
print('El total es: ','$',total,file=file1)
print('------------------------------------',file=file1)
file1.close()

print('Su total es:','$ ',total)
print('Enseguida se imprimira su recibo')





