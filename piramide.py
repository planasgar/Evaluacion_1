def piramide(filas=8):
    espacios=' '
    asteriscos='*'
    for i in range(filas):
        for nespacios in range(1,filas-i-1):
            espacios=espacios+' '
        for nasteriscos in range(1,2*i):
            asteriscos=asteriscos+'*'
        print  espacios + asteriscos
        espacios=' '
        asteriscos='*'


piramide(12)
