#ivan araluce nava A00949193
#username
#29/03/2016

import random

def username(nombre,apellidop,apellidom):
    numSigno=random.randint(35,38)
    simbolo=chr(numSigno)
    numero=random.randint(1,9)
    usuario=apellidop[0:5]+apellidom[0:3]+nombre[0]+simbolo+str(numero)
    return usuario

#programa principal
nombre=input("nombre:")
apellidop=input("apellido paterno:")
apellidom=input("apellido materno:")
nombre_usuario=username(nombre,apellidop,apellidom)
print("tu nombre de usuario es:", nombre_usuario)
