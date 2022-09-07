from unicodedata import name


class robot:
    _encendido = False # _ indica que no debe ser modificada fuera de la clase
    def __init__(self, nombre):
        self.name = nombre
    def enciende(self): #prennde robot
        self._encendido=True #con el self accedo a la variable de la clase
    
    def apaga(self): #apaga robot
        self._encendido=False

    def estado(self): #devuelve estado del robot(apagado o encendido) 
        return self._encendido

class perro(robot): #hereda caracteristicas y metodos de la clase robot
    pass



robot1=robot('Benjamin') #inicializo nombre(constructor)
print(robot1.name)

robot2=robot('Juan')
print(robot2.name)