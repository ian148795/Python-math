def dolares_pesos(d): #parametro
    pesos=d*18.84
    return pesos
#programa rincipal
cantidad_pesos=dolares_pesos(100)#argumento
print("$100 dolares equivale a:", cantidad_pesos, "pesos")
cantidad_pesos=dolares_pesos(150)#argumento
print("$150 dolares equivale a:", cantidad_pesos,"pesos")
cantidad_dolares_str=input("dolares:")
cantidad_dolares=float(cantidad_dolares_str)
cantidad_pesos=dolares_pesos(cantidad_dolares)#argumento
print("con:", cantidad_dolares, "dolares tienes:", cantidad_pesos,"pesos")
