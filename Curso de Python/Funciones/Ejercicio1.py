import math
from xml.etree.ElementTree import PI

def area_triangulo(base, altura):
    area = (base*altura)/2
    return area

def area_circulo(radio):
    area = math.pi*(radio**2)
    return area

print('El area del triangulo es ', area_triangulo(2,4))
print('El area del circulo es ', area_circulo(6))