def validaRFC(palabra):
    longitud=len(palabra)
    letras=palabra[0:4]
    numeros=palabra[4:]
    if longitud==10 and letras.isalpha() and numeros.isdigit():
        return True
    else:
        print("RFC no valido")
        return False

#programa principal
rfc=input("RFC:")
while not(validaRFC(rfc)):
    rfc=input("RFC:")
print("RFC Valido")
