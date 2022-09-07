class motor():
    tipo = 'Diesel'
class rueda():
    cantidad = 4
    rodado = 24
class puertas():
    cantidad = 5
class carroceria():
    puertas = puertas()
    ruedas = rueda()
class auto():
    motor = motor()
    carroceria = carroceria()


auto1 = auto()

print(auto1.carroceria.ruedas.rodado)