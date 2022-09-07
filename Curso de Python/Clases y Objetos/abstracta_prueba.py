from abc import ABC, abstractclassmethod, abstractmethod

class animal(ABC):
    @abstractmethod
    def sonido(self):   #indico que sonido es un metodo abstracto, por lo atnto
        pass        #las clases que hereden a animal deben tenerlo tambien


class perro(animal):
    def sonido(self):
        print('GUAU')

class gato(animal):
    def sonido(self):
        print('MIAU')

perro1 = perro()
perro1.sonido()

gato1= gato()
gato1.sonido()
