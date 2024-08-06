#procedimeiento menu
def menu():
    print("evaluacion de polinomios")
    print("1) evaluacion de polinomios predefinidos")
    print("2) Polinomio lineal")
    print("3) Polinomio cuadratico")

def solicita_opcion():
    opcion_str=input("Opcion:")
    return int(opcion_str)

def evalua_funcion(tipo,a,b,c,x):
    if(tipo==1):
        resultado=a*x+b
    else:
        resultado=a*x**2+b*x+c
    return resultado

def 
#programa principal
menu()
opcion=solicita_opcion()
if(opcion==1):
    evaluacion_predefinida()
