#programa principal
mensaje = input("introduce el mensaje")

#programa para recorrer el nombre
string_numeros=""
for character in mensaje:
    if character in "1234567890":
        string_numeros= string_numeros+character

print("digitos:" + string_numeros)

