#funcion para calcular grados fahrenheit en base a grados celsius
def celsius_a_fahrenheit(grados_celsius):
   f= grados_celsius*1.8+32
   return f


print("conversion de grados celsius a grados fahrenheit")
celsius = float(input("temperatura en grados C:"))
fahrenheit = celsius_a_fahrenheit(celsius)
print("la temperatura correspondiente a ", celsius, "grados celsius en fahrenheit es ", fahrenheit)
