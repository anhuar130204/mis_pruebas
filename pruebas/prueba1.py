"""
   Prueba1
   Nombre:Anhuar Fernando MI                                              
   Fecha: 02/02/2023                                                      
   Descripcion:piramide de nuemros
"""
numero=int(input("introduzca un numero:  "))   # se pide un numero entero

NUMCOL=0    # "se declara la constante numero de columnas para la piramide"

while NUMCOL<numero: # se introduce la condicion mientras el numero de columnas sea menor al numero pedido entoces
    fila=NUMCOL+1   # se declara la viarable fila para determinar el numero de columnas + 1
    CONTADOR=0  # se declara la constante contador igual a 0
    m="" # se ocupa la variable m para ocupar como un caracter
    while(CONTADOR<fila):   # se introduce la condicion while para la condicion sea contador menor a fila
        m=m+str(NUMCOL+1)+" "  # se declara la viariable m es iagual a valor de m + el valor de NUMCOL
        CONTADOR+=1    # se declara la constante CONTADOR +1 con el valor anterior
    print (m)    # se manda imprimir la variable m
    NUMCOL += 1   # se declara la contante de NUMCOL + 1 sobre le valor anterior
   
    