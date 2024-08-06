def NombreUsuario(nombreUsuario):
    if len(nombreUsuario) <6:
        return("El nombre de usuario debe tener al menos 6 caracteres")
    elif len(nombreUsuario) >12:
        return("el nombre de usuario debe tener maximo 12 caracteres")
    elif nombreUsuario.isalnum()== False:
        return("el nombre de usuario puede contener solo letras y numeros")
    else:
        return True

def validaContraseña(contraseña):
    if len(contraseña)!= 8:
        return("La contraseña debe tener 8 caracteres")
    elif contraseña.isalnum()== True:
        return("Contraseña no segura")
    elif contraseña.isalpha()== True:
        return("Contraseña no segura")
    elif contraseña.isdigit()== True:
        return("Contraseña no segura")
    elif " " in contraseña:
        return("La contraseña no debe tener espacios")
    else:
        return True


#programa principal
us=input("usuario:")
while(NombreUsuario(us))!= True:
    print(NombreUsuario(us))
    us=input("usuario:")

cont=input("contraseña:")
while(validaContraseña(cont))!= True:
    print(validaContraseña(cont))
    cont=input("contraseña:")
    

 
