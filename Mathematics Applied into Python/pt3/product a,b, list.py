def dotproduct(a,b):
    suma=0
    for i in range(0,len(a)):
        multi=a[i]*b[i]
        suma = suma+multi
    return suma

print(dotproduct([], []))
print(dotproduct([1, 2, 3], [4, 5, 6]))
print(dotproduct([1.3, 3.4, 5.7, 9.5, 10.4], [-4.5, 3.0, 1.5, 0.9, 0.0]))
print(dotproduct([92, -39, 82, 16, -64, -1, -16, -45, -7, 39, 45, 0, 34, -3, -51, 71, 23, -8, 41, -40], [-50, -81, 94, -84, 47, 86, 52, 19, -57, 36, -20, 11, -42, 48, 14, 13, 9, -67, 92, 96]))
