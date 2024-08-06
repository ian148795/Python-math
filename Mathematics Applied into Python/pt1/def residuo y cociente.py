def calcula_cociente_residuo(dividiendo, divisor):
    cociente=dividiendo//divisor
    residuo=dividiendo%divisor
    return (cociente, residuo)

(cociente, residuo)= calcula_cociente_residuo(9,7)
print("cociente="+str(cociente)+"\nResiduo="+str(residuo))
