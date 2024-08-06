#ivan araluce nava A00949193
#tabla distancia
#07/03/2016
#funcion for ciclo

def millas_a_km(x):
    m=x*1.609
    return m
#programa principal
for i in range(100,1100,100):
    kilometros=millas_a_km(i)
    print(i,"millas:", kilometros,"Km")
    
