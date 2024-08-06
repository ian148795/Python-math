#Proyecto final de programacion - (Listado de una orden y precio final en Cafe Starbucks)
# 11 de Mayo del 2016
# A00949193 Iván Araluce Nava
# A01232295 Ivana Boehringer Russek
# A01232828 Gabriel Marcos Bracho

#Descripcion del proyecto:


#Funcion busca_precio para saber el precio de la bebida.
def busca_precio(nombre,listanombres, listaprecios):
    precio=0
    for i in range(0,len(listanombres)):
        n=listanombres[i]
        nom=n[0:len(n)-1]
        if nom==nombre:
            precio=listaprecios[i]

    return precio

def sumatotal(x):
    contador = 0 
    for i in x:
        contador = i[1]+contador
    return contador

#Programa Principal
#Inicio de presentacion
titulo="-¡Bienvenido a Starbucks!-"
print(titulo.center(70))

#menu
menu=open('menu.txt','r')
contenido_menu=menu.read()
print(contenido_menu)
menu.close()

#orden
lista = []
orden = input("¿Que desea ordenar?: ")
while orden not in 'abcdefghijklmnopqrst':
    print('Esa opcion no existe, intenta de nuevo.')
    orden=input('¿Que deseas ordenar? ')
if orden == 'a':
    paq =('Berry Refresher', 49)
    lista.append(paq)
elif orden == 'b':
    paq =('Lemon Refresher', 49)
    lista.append(paq)
elif orden == 'c':
    paq =('Te Chai', 45)
    lista.append(paq) 
elif orden == 'd':
    paq =('Chamomile', 45)
    lista.append(paq)
elif orden == 'e':
    paq =('Te Verde', 45)
    lista.append(paq)
elif orden == 'f':
    paq =('English Breakfast', 45)
    lista.append(paq)
elif orden == 'g':
    paq =('Caramel Frapuccino', 52)
    lista.append(paq)
elif orden == 'h':
    paq =('Mocha Frapuccino', 52)
    lista.append(paq)
elif orden == 'i':
    paq =('Cajeta Frapuccino', 52)
    lista.append(paq)
elif orden == 'j':
    paq =('Cafe Frapuccino', 52)
    lista.append(paq)
elif orden == 'k':
    paq =('Chip Frapuccino', 52)
    lista.append(pag)
elif orden == 'l':
    paq =('Te chai Frapuccino', 52)
    lista.append(paq)
elif orden == 'm':
    paq =('Mocha Coconut', 54)
    lista.append(paq)
elif orden == 'n':
    paq =('Flat White', 52)
    lista.append(paq)
elif orden == 'o':
    paq =('Capuccino', 50)
    lista.append(paq)
elif orden == 'p':
    paq =('Espresso Americano', 42)
    lista.append(paq)
elif orden == 'q':
    paq =('Helado Espresso Americano', 45)
    lista.append(paq)
elif orden == 'r':
    paq =('Cafe Mocha', 52)
    lista.append(paq)
elif orden == 's':
    paq =('Helado Cafe Mocha', 52)
    lista.append(paq)
elif orden == 't':
    paq =('Cafe Latte', 42)
    lista.append(paq)
    


#orden para agregar algo mas
agreg = input("¿Desea agregar algo mas a su orden?(si/no): ")
while agreg not in('si') and agreg not in ('no'):
   print('Esa opcion no existe, intenta de nuevo') 
   agreg = input("¿Desea agregar algo mas a su orden?(si/no): ")
while agreg !='no':
    agregar = input("¿Que desea agregar?: ")
    if agregar not in 'abcdefghijklmnopqrst':
        print('Esa opcion no existe, intenta de nuevo')
        agregar = input('¿Que desea agregar? ')
    if agregar == 'a':
        paq =('Berry Refresher', 49)
        lista.append(paq)
    elif agregar == 'b':
        paq =('Lemon Refresher', 49)
        lista.append(paq)
    elif agregar == 'c':
        paq =('Te Chai', 45)
        lista.append(paq) 
    elif agregar == 'd':
        paq =('Chamomile', 45)
        lista.append(paq)
    elif agregar == 'e':
        paq =('Te Verde', 45)
        lista.append(paq)
    elif agregar == 'f':
        paq =('English Breakfast', 45)
        lista.append(paq)
    elif agregar == 'g':
        paq =('Caramel Frapuccino', 52)
        lista.append(paq)
    elif agregar == 'h':
        paq =('Mocha Frapuccino', 52)
        lista.append(paq)
    elif agregar == 'i':
        paq =('Cajeta Frapuccino', 52)
        lista.append(paq)
    elif agregar == 'j':
        paq =('Cafe Frapuccino', 52)
        lista.append(paq)
    elif agregar == 'k':
        paq =('Chip Frapuccino', 52)
        lista.append(pag)
    elif agregar == 'l':
        paq =('Te chai Frapuccino', 52)
        lista.append(paq)
    elif agregar == 'm':
        paq =('Mocha Coconut', 54)
        lista.append(paq)
    elif agregar == 'n':
        paq =('Flat White', 52)
        lista.append(paq)
    elif agregar == 'o':
        paq =('Capuccino', 50)
        lista.append(paq)
    elif agregar == 'p':
        paq =('Espresso Americano', 42)
        lista.append(paq)
    elif agregar == 'q':
        paq =('Helado Espresso Americano', 45)
        lista.append(paq)
    elif agregar == 'r':
        paq =('Cafe Mocha', 52)
        lista.append(paq)
    elif agregar == 's':
        paq =('Helado Cafe Mocha', 52)
        lista.append(paq)
    elif agregar == 't':
        paq =('Cafe Latte', 42)
        lista.append(paq)    
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






        


