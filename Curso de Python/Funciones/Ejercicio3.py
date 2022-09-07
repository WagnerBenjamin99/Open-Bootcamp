def esBisiesto(año):
    if año % 4 == 0 and año % 100 != 0:
        return True
        if año % 100 == 0 and año % 400 == 0:
            return True
    
    if año % 4 == 0:
        if año % 100 == 0 and año % 400 != 0:
            return False
        if año % 100 != 0 and año % 400 == 0: 
            return False
    
    if año % 4 != 0:
        if año % 100 != 0 or año % 400 != 0:
            return False
    
if esBisiesto(2016) == False:
    print('El año no es bisiesto')
else:
    print('El año es bisiesto')