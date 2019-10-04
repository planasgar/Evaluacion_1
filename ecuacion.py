#En este programa le pedimos al usuario que teclee los coeficientes de un polinomioy hallamos el valor de las raices
import math
def ecuacion():
    print "Introduzca los coeficientes del polinomio"
    print "a*x^2+b*x+c"
    a=input("a= ")
    b=input("b= ")
    c=input("c= ")
    radicando=b*b-4*a*c
    if (radicando>0):
        raiz1=(-b+math.sqrt(radicando))/(2*a)
        raiz2=(-b-math.sqrt(radicando))/(2*a)
        print "primera solucion ="
        print raiz1
        print "segunda solucion ="
        print raiz2
    else:
        print "No tiene solucion"

ecuacion() 
