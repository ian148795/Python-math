def muestra_datos():
    print("programa realizado por:")
    print("Ivan Araluce Nava")
    print("Matricula: A00949193")
    print("Carrera: IMT")

def muestra_menu():
    print("\nCalculo de indice de masa corporal y calorias recomendadas")
    print("1) Cálculo con datos previamente definidos")
    print("2)	Cálculo de IMC")
    print("3)	Cálculo de calorías recomendadas")
    print("4)	IMC y Calorías recomendadas")
    print("5)	Terminar")

def solicita_opcion():
    opcion_str=input("opcion:")
    return (int(opcion_str))

def calcula_imc(peso, altura):
    imc= peso/altura**2
    return imc

def calcula_con_datos_definidos():
    peso= 30
    altura= 120
    sexo= "F"
    dias_ejercicio=3
    edad= 9
    imc= calcula_imc(peso,altura)
    print("peso = 30, altura=120, sexo= f, dias de ejercicio= 3, edad=9")
    print("IMC=", imc)
#programa principal
muestra_datos()
muestra_menu()
opcion= solicita_opcion()
if(opcion==1):
    calcula_con_datos_definidos()
else:
    if(opcion==2):
        calcula_imc()
