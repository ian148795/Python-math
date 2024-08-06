
def user_name(nombre, apellido):
    ap=apellido[:12]
    inicio = nombre[0]
    return ap+inicio+"1"

#programa principal
nombre = input("nombre:")
apellido = input("apellido:")
print(user_name(nombre, apellido))
