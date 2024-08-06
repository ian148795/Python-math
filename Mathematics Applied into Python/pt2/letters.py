#ivan araluce nava A00949193
#letters
#29/03/2016

nombre=input("ingresa tu nombre:")
string_vocales=""
string_consonantes=""
for caracter in nombre:
    if caracter in "aeiouAEIOU":
        string_vocales=string_vocales+caracter
    else:
        if caracter!=" ":
            string_consonantes=string_consonantes+caracter
print("vocales:"+string_vocales)
print("consonantes:"+string_consonantes)
