suma=0
print("\nSuma de numeros\n")
continuar='s'
while(continuar =='s'):
    num=int(input("Dame un numero:"))
    suma= suma + num
    continuar=""
    while continuar!="n" and continuar!= "s":
        continuar = input("desea continuar (s/n)?")
        continuar = continuar.lower()
print("\nEl valor de la suma es", suma)
