#Ivan Araluce Nava A00949193

def muestra_datos():
    print(" Ivan Araluce Nava, A00949193, IMT")

def indice_masa_corporal(kg, m):
    imc = (kg/m**2)
    if imc<18.5:
        print("bajo peso")
    elif imc>18.5 and imc<24.9:
        print("peso normal")
    elif imc>25 and imc<29.9:
        print("preobesidad")
    elif imc>30 and imc<34.9:
        print("obesidad grado 1")
    elif imc>35 and imc<39.9:
        print("obesidad grado 2")
    elif imc>40:
        print("obesidad grado 3")

def tasaMetabolicaBasal(peso, altura, edad, sexo):

    if sexo=='masculino':
        tmb=66+(13*peso)+(5*altura)-(6.8*edad)
    elif sexo=='femenino':
        tmb655+(9.6*peso)+(1.8*altura)-(4.7*edad)
        return tmb
def calorias_diarias_recomendadas(tmb,ejercicio):
    if ejercicio==0:
        calorias=tmb*1.2
    elif ejercicio>0 or ejercicio<=3:
        calorias=tmb*1.375
    elif ejercicio<=5:
        calorias=tmb*1.55
    elif ejercicio<=7:
        calorias=tmb*1.725
    return calorias

#programa principal
muestra_datos()
peso = int(input("introduce el peso"))
altura = int(input("introduce la altura"))
indice_masa_corporal(peso, altura)
edad = int(input("edad:"))
tasaMetabolicaBasal(peso, altura, edad, sexo)
sexo = int(input("sexo:"))
calorias_diarias_recomendadas(tmb, ejercicio)



             
             
