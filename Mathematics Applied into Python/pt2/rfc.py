#ivan araluce nava
#rfc
#18/03/2016
def generaRFC(apellido_paterno,apellido_materno,nombre,dia,mes,año):
    rfc=apellido_paterno[0:2]+apellido_materno[0]+nombre[0]+año[2:4]+mes+dia
    return rfc
#programa principal

continuar="si"
while(continuar=="si"):
    apellido_p=input("apellido paterno:")
    apellido_m=input("apellido materno:")
    name=input("nombre:")
    ano=input("año de nacimiento:")
    month=input("mes:")
    day=input("dia:")
    rfc=generaRFC(apellido_p,apellido_m,name,ano,month,day)
    print(rfc.upper())
    continuar=input("desea continuar?")
    continuar=continuar.lower()
    print("gracias")
    
    
