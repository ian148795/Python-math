def duplica(palabra):
    dup=""
    for x in palabra:
        dup+=x*2
    return dup
        
#programa principal
y= input("ingrese la palabra")
print(duplica(y)) 
