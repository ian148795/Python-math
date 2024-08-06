# -*- coding: utf-8 -*-
import numpy as np
from scipy import linalg
from sympy import *

def eval_funcion(funcion,xi,yi):
    x,y= symbols("x y")
    return float(funcion.subs([(x,xi),(y,yi)]))

def solucion_2sistec_no_lineales(funcion1,funcion2,es,xi,yi,max_it):
    x,y= symbols("x y")
    #Obtener elementos del jacobiano
    f=sympify(funcion1)
    g=sympify(funcion2)
    fx=diff(f,x)
    fy=diff(f,y)
    gx=diff(g,x)
    gy=diff(g,y)
    print("fx="+str(fx),"fy="+str(fy))
    print("gx="+str(gx),"gy="+str(gy))
    eax = 100
    eay = 100
    i=0
    while (((eax > es) or (eay > es)) and (i < max_it)):
        #Evaluar jacobiano - Matriz A
        A = np.array([[eval_funcion(fx,xi,yi),eval_funcion(fy,xi,yi)],
                      [eval_funcion(gx,xi,yi),eval_funcion(gy,xi,yi)]])
        #Evaluar 
        B = np.array([[-1*eval_funcion(f,xi,yi)],[-1*eval_funcion(g,xi,yi)]])
       
        delta = linalg.solve(A,B)
        deltax = delta[0]
        deltay = delta[1]
        
        xn = xi + deltax
        yn = yi + deltay

        eax = abs((deltax/xn)*100)
        eay = abs((deltay/yn)*100)
       
       
        print("-----Iteración "+str(i+1)+"-----")
        print("xi = ",xi, "\tDelta x = ",deltax,"\txn= ",xn,"eax = ",eax,"%")
        print("yi = ",yi, "\tDelta y = ",deltay,"\tyn= ",yn,"eay = ",eay,"%")
        i=i+1
        xi=xn
        yi=yn
    return i,xi,yi,eax,eay

def main ():
    print("-----Resolución de sistema de dos ecuaciones no lineales por método de Newton")
    f = input("Función 1:")
    g = input("Función 2:")
#   f=5x1**2-x2**2=0
#   g=x2-0.25(senx1+cosx2)=0

    print("Valor inicial:")
    x0 = float(input("X0 = "))
    y0 = float(input("Y0 = "))
  
    es= float(input("Tolerancia (%): "))
    max_i = int(input("Número máximo de iteraciones : "))
    i,x,y,eax,eay=solucion_2sistec_no_lineales(f,g,es,x0,y0,max_i)
    print("Resultados:")
    print("x=",x,"y=",y,"eax=",eax,"eay=",eay,"Iteraciones=",i)

main()
