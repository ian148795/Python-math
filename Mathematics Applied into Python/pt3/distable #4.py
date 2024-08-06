#4 distable

def miles_to_km(m):
    km = m*1.609
    return km
for m in range(100,1100,100):
    km=miles_to_km(m)
    print(m, "miles =" ,km, "km")
