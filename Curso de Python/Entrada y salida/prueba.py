numero = 1 
string = 'Hola mundo'
booleano = True

def suma(x, y):
    return x + y

print('La cadena es {}, el numero es {} y el booleano {}'.format(string, numero, booleano))

#emprimiendo por indice
print('La cadena es {2}, el numero es {1} y el booleano {0}'.format(booleano, numero, string))

#imprimiendo por keys
print('La cadena es {str}, el numero es {num} y el booleano {bool}'.format(str=string, num = numero, bool = booleano))

#FORMA MAS HABITUAL
print(f'El numero es {numero}, la suma es {suma(numero, 10)}')