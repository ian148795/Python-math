#Ivan Araluce Nava A00949193
#molecules

def molecula(formula):
    for caracter in formula:
        if(caracter=='H'):
            print("Hidrogeno:",end=" ")
        else:
            if(caracter=='O'):
                print("Oxigeno:", end=" ")
            else:
                if(caracter=="C"):
                    print("Carbono",end=" ")
                else:
                    print(caracter)


#programa principal
formula=input("ingresa tu formula:")
molecula(formula)
if(formula=="H201"):
    print("Agua")
else:
    if(formula=="H202"):
        print("Peroxido de Hidrogeno")
    else:
        if(formula=="C2H601"):
            print("Etanol")
            
