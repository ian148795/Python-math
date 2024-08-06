def area_triangulo(b,h):
    area = b*h/2
    return area
#programa principal

print("area de triangulo")
area_a = area_triangulo(4,8)
print(area_a)

b = int(input("base:"))
h = int(input("altura:"))
print("area de triangulo:" , b*h/2)
