class alumno():
    def __init__(self, nombre, nota): 
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print(self.nombre)
        print(self.nota)
    def resultado(self):
        if self.nota >= 6:
            print('APROBADO')
        else:
            print('DESAPROBADO')

alumno1 = alumno('Franco', 6)
alumno1.imprimir()
alumno1.resultado()
