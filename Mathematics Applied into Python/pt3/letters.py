
#programa principal
nombre = input("ingrese nombre")

#ciclo para recorrer los caracteres del nombre
string_vocales=""
string_consonantes=""
for character in nombre:
    if character in "aeiouAEIOU":
        string_vocales = string_vocales+character
    else:
        string_consonantes = string_consonantes+character
print("vocales"+string_vocales)
print("Consonantes"+string_consonantes)

      
