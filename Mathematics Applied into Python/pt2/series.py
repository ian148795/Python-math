def series(n):
    serie=((n+1)**3-n**3)
    return serie
#programa principal
for i in range(1,13,3):
    serie=series(i)
    print(serie)
