class robot:
    _encendido = False # _ indica que no debe ser modificada fuera de la clase

    def enciende(self): #prennde robot
        self._encendido=True #con el self accedo a la variable de la clase
    
    def apaga(self): #apaga robot
        self._encendido=False

    def estado(self): #devuelve estado del robot(apagado o encendido) 
        return self._encendido


robot1=robot()

print(robot1.estado)