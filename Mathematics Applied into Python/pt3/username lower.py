def username(prim, media, final):
    primera = prim[0]
    mediana = media[1]
    fin = final[:6]
    return primera.lower()+mediana.lower()+final.lower()
#programa principal
print(username('Scarlett', 'Ingrid', 'Johansson'))
print(username('Donald', 'Ervin', 'Knuth'))
print(username('Alan', 'Mathison', 'Turing')) 
print(username('Martin', 'Luther', 'King')) 
print(username('Stephen', 'William', 'Hawking'))
print(username('Alejandro', 'Gonzalez', 'Inarritu')) 
