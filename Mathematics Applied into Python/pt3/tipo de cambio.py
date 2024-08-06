#conversion de dolares a pesos y euros
#paso 1 pedir la cantidad de dolares, pesos y euros
# paso 2 convertir a pesos y euros
# paso 3 realizar la formula
# paso 4 pedir la conversion

dolar_str = input ("dolar:")
peso_str = input ("peso:")
euro_str = input ("euro:")
dolar_int = int (dolar_str)
peso_int = int (peso_str)
euro_int = int (euro_str)

resultado = (dolar_int*peso_int)
resultadoo = (dolar_int*euro_int)

print ("resultado de tipo de cambio", resultado, resultadoo)

