
def encode(msg):
    string="" #inicializar sting en vacio
    for character in msg:
        num = ord(character)
        string = string + " "+ str(num)
    return string

#programa principal
print(encode("ABC"))
