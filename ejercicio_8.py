def ejercicio_8():
    print "De que precio quieres sacar el IVA"
    a=input("precio")
    print "¿Qué tipo de IVA quieres aplicarle: General, Reducido o Superreducido?"
    b=raw_input("Tipo de IVA= ") 
    if (b=="general"):
        b=16
    if (b=="reducido"):
        b=7
    if (b=="superreducido"):
        b=4

    precio=a+a*(b*0.01)
    print precio, "euros"

ejercicio_8()
    
    
