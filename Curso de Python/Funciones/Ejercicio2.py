def esPrimo(numero):
    contador = 0
    for i in range (1, numero):
        if(i != 1 and i != numero):
            if(numero%i == 0):
                contador = contador + 1
    if contador > 0:
        return False
    else:
        return True

if(esPrimo(6) == False):
    print('El numero no es primo')
else:
    print('El numero es primo')
        