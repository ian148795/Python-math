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
    if opcion=='a':
        nombre='Berry Refresher'
    else:
        if opcion=='b':
            nombre= 'Lemon Refresher'
        else:
            if opcion=='c':
                nombre='Te Chai'
            else:
                if opcion=='d':
                    nombre='Chamomile'
                else:
                    if opcion=='e':
                        nombre='Te Verde'
                    else:
                        if opcion=='f':
                            nombre='English Breakfast'
                        else:
                            if opcion=='g':
                                nombre='Caramel Frapuccino'
                            else:
                                if opcion=='h':
                                    nombre='Mocha Frapuccino'
                                else:
                                    if opcion=='i':
                                        nombre='Cajeta Frapuccino'
                                    else:
                                        if opcion=='j':
                                            nombre='Cafe Frapuccino'
                                        else:
                                            if opcion=='k':
                                                nombre='Chip Frapuccino'
                                            else:
                                                if opcion=='l':
                                                    nombre='Te chai Frapuccino'
                                                else:
                                                    if opcion=='m':
                                                        nombre='Mocha Coconut'
                                                    else:
                                                        if opcion=='n':
                                                            nombre='Flat White'
                                                        else:
                                                            if opcion=='o':
                                                                nombre='Capuccino'
                                                            else:
                                                                if opcion=='p':
                                                                    nombre= 'Espresso Americano'
                                                                else:
                                                                    if opcion=='q':
                                                                        nombre='Helado Espresso Americano'
                                                                    else:
                                                                        if opcion=='r':
                                                                            nombre='Cafe Mocha'
                                                                        else:
                                                                            if opcion=='s':
                                                                                nombre='Helado Cafe Mocha'
                                                                            else:
                                                                                if opcion=='t':
                                                                                    nombre='Cafe Latte'
                                                                                else:
                                                                                    print("Esa opcion no existe")

                                                                                
                                                                                    
        return nombre

       

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
productos.close()

#precios
precios=open('precios.txt','r')
listaprecios=precios.readlines()
precios.close()

#mandar llamar funcion busca_nombre
opcion=input('Hola! Que deseas ordenar?')
while opcion not in 'abcdefghijklmnopqrst':
    print('Opcion no valida, intenta de nuevo')
    opcion=input('Hola! Que deseas ordenar?')
nombre=busca_nombre(opcion)
print(nombre)
    
#mandar llamar funcion busca_precio
precio= busca_precio(nombre,listanombres,listaprecios)
print('Precio: $: ', precio)


#Agregar bebidas extras... ESTO ES LO QUE NO ESTA BIEN,,, PERO MASOMENOS ES ASI SEGUN YO SOLO QUE FALTA QUE SE SIGA CORRIENDO EL CICLO LAS VECES QUE QUIERAS###
agregar= input('Desea agregar algo mas a la orden?(si/no) ')
opcion=input('Que mas deseas?')
while agregar != ('si') and agregar!= ('no'):
    print('Esa opcion no existe, intentar con si y no')
    opcion=input('Que mas deseas?')
    agregar= input('Desea agregar algo mas a la orden?(si/no) ')
    opcion=input('Que mas deseas?')
    while opcion not in 'abcdefghijklmnopqrst':
        
        print('Opcion no valida, intenta de nuevo')
        opcion=input('Hola! Que deseas ordenar?')
nombre=busca_nombre(opcion)
print(nombre)
precio= busca_precio(nombre,listanombres,listaprecios)
print('Precio: $: ', precio)




    
if agregar=='no':
    print('Gracias por su compra, sus bebidas son: ', ) #lista de bebidas
    print('Total: ', ) #total de precios
        


## LO QUE FALTA ES LO DE CONTINUAR O NO Y LAS LISTAS DE BEBIDAS Y TOTAL##

        


