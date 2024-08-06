#obtener la masa
# paso 1 pedir el peso y la altura
#paso 2 aplicar la formula
# paso 3 mostrar el resultado

peso_str = input ("peso:")
altura_str = input ("altura:")
peso_int = int (peso_str)
altura_int = int (altura_str)

resultado = (peso_int/altura_int**2)

print ("indice de masa corporal", resultado)
            
