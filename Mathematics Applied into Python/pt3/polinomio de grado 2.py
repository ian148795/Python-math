#polinomio de grado 2
# paso 1 pedir el valor de a, b, c y x
# paso 2 aplicar la formula
# paso 3 mostrar el resultado

a_str = input ("a:")
b_str = input ("b:")
c_str = input ("c:")
x_str = input ("x:")
a_int = int (a_str)
b_int = int (b_str)
c_int = int (c_str)
x_int = int (x_str)

resultado = (a_int*x_int**2+b_int*x_int+c_int)

print ("resultado de grado 2" , resultado)
