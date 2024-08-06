ingreso=int(input("ingresos:"))

if (ingreso >=0 and ingreso <=4000):
    impuesto=0.0
else:
    if (ingreso<=4000 and ingreso<=29000):
            impuesto=0.15
    else:
        if (ingreso <=29000 and ingreso<=70000):
                impuesto=0.25
        else:
            if (ingreso>70000):
                    impuesto=.35

ingreso_impuesto=ingreso*(1+impuesto)
print("tienes ingresos de:", ingreso, "debes pagar:", impuesto, "lo que seria un total de:", ingreso_impuesto)



    
