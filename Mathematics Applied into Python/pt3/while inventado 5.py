import random
x = random.randint(1,25)
print("adivina el numero de la letra de la persona que me gusta:")
letra = int(input("introduce numero de la letra:"))

while letra!=x:
    if (letra<x):
        print("estas muy abajo del abedecedario con el numero")
    elif(letra>x):
        print("estas muy arriba del abedecedario con el numero")
    letra=int(input("introduce el numero de la letra"))
print("adivinaste ;)")
