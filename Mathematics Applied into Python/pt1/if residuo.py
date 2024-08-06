num=int(input("dame un numero:"))
resi1=num%2
resi2=num%3
resi3=num%4
resi4=num%5

if (num<2) or (num<3) or (num<4) or (num<5):
    print("no son divisibles entre los numeros 2, 3, 4 y 5")
else:
    if (resi1==0) and (resi2==0) and (resi3==0) and (resi4==0):
        print("el numero:", num, "es divisible entre 2,3,4,5")
    else:
        if(resi1==0) and (resi2==0) and (resi3==0):
            print("el numero:", num,"es divisible entre 2,3,4")
        else:
            if(resi1==0) and (resi2==0) and (resi4==0):
                print("el numero:", num, "es divisible entre 2,3,5")
            else:
                if (resi1==0) and (resi2==0):
                    print("el numero:", num, "es divisible entre 2,3")
                else:
                    if(resi1==0) and (resi3==0):
                        print("el numero:", num, "es divisible entre 2,4")
                    else:
                        if(resi1==0) and (resi4==0):
                            print("el numero:", num,"es divisible entre 2,5")
                        else:
                            if(resi2==0) and (resi3==0):
                                print("el numero:", num, "es divisible entre 3,4")
                            else:
                                if (resi2==0) and (resi4==0):
                                    print("el numero:", num,"es divisible entre 3,5")
                                else:
                                    if(resi3==0) and (resi4==0):
                                        print("el numero:", num, "es divisible entre 4,5")
                                        
        
