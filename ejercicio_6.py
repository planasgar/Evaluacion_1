def ejercicio_6():
    print "Dime 2 numeros:"
    a=input("a= ")
    b=input("b= ")
    print "Ahora dime que operacion deseas realizar suma (s), resta (r), multiplicacion (m) o division(d)"
    operacion=raw_input("operacion= ")
    if (operacion=="s"):
        print "resultado=", a+b
    if (operacion=="r"):
        print "resultado=", a-b
    if (operacion=="m"):
        print "resultado=", a*b
    if (operacion=="d"):
        print "resultado=", a/b
ejercicio_6()
