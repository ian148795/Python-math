def potencias2(n):
    x=0
    lista=[]
    while 2**x<=n:
        lista.append(2**x)
        x+=1
    return lista
print(potencias2(100))
print(potencias2(-1))
