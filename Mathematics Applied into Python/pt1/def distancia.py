#ivan araluce nava
# funcion, distancia
# 12/02/2016

def calcula_distancia(v, t):
    g=9.81
    resultado =v*t(1/2)*g*t**2
    return resultado
#programa principal
v_str=input("velocidad:")
v=int(v_str)
t_str=input("tiempo:")
t=int(t_str)
distancia= calcula_distancia(v, t)
print("tu distancia recorrida es:", distancia,"metros", "en:", t, "segundos")


