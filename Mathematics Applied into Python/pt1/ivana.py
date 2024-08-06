categoria_str=input("dame tu categoria:")
categoria_int=int(categoria_str)
saldo_actual_str=input("ingresa tu saldo actual:")
saldo_actual_int=int(saldo_actual_str)

if (categoria_int==1):
    nuevosaldo= saldo_actual_int+ saldo_actual_int*1.15
else:
    if (categoria_int==2):
        nuevosaldo= saldo_actual_int+ saldo_actual_int*1.10
    else:
        if (categoria_int==3):
            nuevosaldo= saldo_actual_int+saldo_actual_int*1.08
        else:
            if (categoria_int==4):
                nuevosaldo= saldo_actual_int+saldo_actual_int*1.07

print("saldo actual:", saldo_actual_int)
print("nuevo saldo:", nuevosaldo)
