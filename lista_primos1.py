def lista_primos():
    print "Porque numero quieres que empieze?"
    a=input("a= ")
    print "Porque numero quieres que acabe?"
    b=input("b= ")
    divisor=False
    salir=False
    for i in range (a,b):
        print i
        for cont in range(2,i):
            if(i%cont==0):
                divisor=True
                salir=True
            if(salir==True):
                 cont=i
        if(divisor==True):
            print "No es primo"
        else:
            print "Es primo"
        divisor=False
        
    
            
        

lista_primos()
    
