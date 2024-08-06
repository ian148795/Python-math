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

#Funcion busca_nombre para darle nombre a la bebida despues de que el cliente selecciona una letra del menu.

def busca_nombre(opcion):
    file=open('ticket.txt','a')
    if opcion=='a':
        nombre='Berry Refresher $49'
        file.write('49')
    else:
        if opcion=='b':
            nombre= 'Lemon Refresher $49'
            file.write('49')
        else:
            if opcion=='c':
                nombre='Te Chai $45'
                file.write('45')
            else:
                if opcion=='d':
                    nombre='Chamomile $45'
                    file.write('45')
                else:
                    if opcion=='e':
                        nombre='Te Verde $45'
                        file.write('45')
                    else:
                        if opcion=='f':
                            nombre='English Breakfast $45'
                            file.write('45')
                        else:
                            if opcion=='g':
                                nombre='Caramel Frapuccino $52'
                                file.write('52')
                            else:
                                if opcion=='h':
                                    nombre='Mocha Frapuccino $52'
                                    file.write('52')
                                else:
                                    if opcion=='i':
                                        nombre='Cajeta Frapuccino $52'
                                        file.write('52')
                                    else:
                                        if opcion=='j':
                                            nombre='Cafe Frapuccino $52'
                                            file.write('52')
                                        else:
                                            if opcion=='k':
                                                nombre='Chip Frapuccino $52'
                                                file.write('52')
                                            else:
                                                if opcion=='l':
                                                    nombre='Te chai Frapuccino $52'
                                                    file.write('52')
                                                else:
                                                    if opcion=='m':
                                                        nombre='Mocha Coconut $54'
                                                        file.write('54')
                                                    else:
                                                        if opcion=='n':
                                                            nombre='Flat White $52'
                                                            file.write('52')
                                                        else:
                                                            if opcion=='o':
                                                                nombre='Capuccino $50'
                                                                file.write('50')
                                                            else:
                                                                if opcion=='p':
                                                                    nombre= 'Espresso Americano $42'
                                                                    file.write('42')
                                                                else:
                                                                    if opcion=='q':
                                                                        nombre='Helado Espresso Americano $45'
                                                                        file.write('45')
                                                                    else:
                                                                        if opcion=='r':
                                                                            nombre='Cafe Mocha $52'
                                                                            file.write('52')
                                                                        else:
                                                                            if opcion=='s':
                                                                                nombre='Helado Cafe Mocha $52'
                                                                                file.write('52')
                                                                            else:
                                                                                if opcion=='t':
                                                                                    nombre='Cafe Latte $42'
                                                                                    file.write('42')
        return nombre


def sumatotal():
    file2=open('preciofinal.txt','w')
    for eachline in file:
        suma=0
        suma+=eachline
    return suma
    



#Programa Principal
#Inicio de presentacion
titulo="¡Bienvenido a Starbucks!"
print(titulo.center(70))

#menu
menu=open('menu.txt','r')
contenido_menu=menu.read()
print(contenido_menu)
menu.close()

#productos
productos=open('nombreproductos.txt','r')
listanombres=productos.readlines()
print(listanombres)
productos.close()

#precios
precios=open('precios.txt','r')
listaprecios=precios.readlines()
print(listaprecios)
precios.close()

#mandar llamar funcion busca_nombre
opcion=input('Hola! Que deseas ordenar?')
print(opcion)
nombre=busca_nombre(opcion)
print(nombre)

#mandar llamar funcion busca_precio
precio= busca_precio(nombre,listanombres,listaprecios)
print(precio)




#en la pantalla te tiene que dar una lista de lo que pidio el cliente y el total de su cuenta... para esto tenemos que tener un contador para que vaya sumando y que se vaya creando una lista de lo que ordena
#tenemos que poner un while para que si le pica en 'desea ordenar algo mas?' y le picas que si, te vuelva a ensenar el menu, que no tengas que correr el programa otra vez, si le picas no ya te muestra el total
#tiene que tener la opcion de 'ordenar' y opcion de 'terminar' al principio junto con un saludo de 'bienvenido que desea hacer.. etc'


        


