#ivan araluce nava a00949193
#tabla temp
def fahrenheit_a_celsius(gradosF):
    c=(5/9)*(gradosF-32)
    return c
#programa principal
for x in range(-30,71,10):
    celsius=fahrenheit_a_celsius(x)
    print(x, "F=", celsius, "ºC")
