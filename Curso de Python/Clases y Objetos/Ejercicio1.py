class vehiculo():
    color = 'Negro'
    ruedas = 4
    puertas = 5

class Coche(vehiculo):
    velocidad = '200 Km/h'
    cilindrada = '150 Cv'

camaro = Coche()

print(camaro.color)
print(camaro.ruedas)
print(camaro.puertas)
print(camaro.velocidad)
print(camaro.cilindrada)