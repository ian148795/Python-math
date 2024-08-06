#Ivan Araluce Nava A00949193
#ejercicio 2


dia_str = input("dia:")
mes_str = input("mes:")
dia = int(dia_str)
mes = int(mes_str)

if mes==1:
    print("la fecha es", dia, ("de enero"))
elif mes==2:
    print("la fecha es", dia, ("de febrero"))
elif mes==3:
    print("la fecha es", dia, ("de marzo"))
elif mes==4:
    print("la fecha es", dia, ("de abril"))
elif mes==5:
    print("la fecha es", dia ("de mayo"))

else:
    print("error, no corresponde fecha")
    
