from email.policy import default
from django.db import models
from datetime import date

class autor(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nombre

class entrada(models.Model):
    autor = models.ForeignKey(autor, on_delete=models.CASCADE)
    titulo=models.CharField(max_length=200)
    cuerpo=models.CharField(max_length=2000)
    publicacion = models.DateField(default=date.today)
    rating = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.titulo

