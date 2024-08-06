def cuentaDigitos(mensaje):
    digitos=0
    for digi in mensaje:
        if digi.isdigit():
            digitos=digitos+1
    return digitos
#programa principal
mens=input("mensaje:")
print(cuentaDigitos(mens))
