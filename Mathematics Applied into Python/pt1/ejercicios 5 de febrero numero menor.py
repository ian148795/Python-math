print("teclea 3 numeros y te mostrare el menor")

num1=int(input("ingresa el primer numero:"))
num2=int(input("ingresa el segundo numero:"))
num3=int(input("ingresa el tercer numero:"))

if (num1< num2 and num1<num3):
    print("el numero mas chico es:", num1)
if (num2<num1 and num2<num3):
    print("el numero menor es:", num2)
if (num3<num1 and num3<num2):
    print("el numero menor es:", num3)
