palabra = input("ingrese una palabra")
palabra = palabra[::-1]
for character in palabra:
    if palabra in "qwertyuiopasdfghjklñzxcvbnm":
        mayusculas = character.upper()
        print(mayusculas)
    else:
        minusculas = character.lower()
        print(minusculas)
        
