from pyexpat import model
from django.db import models

class comment(models.Model):
    name = models.CharField(max_length=225, null=False)
    score=models.IntegerField(default=3)
    comment=models.CharField(max_length=1000, null=True)
    date=models.DateTimeField(null=True)

    def __str__(self) -> str:
        return self.name

class user(models.Model):
    nombre = models.CharField(max_length=20, null=False)
    apellido = models.CharField(max_length=20, null=False)
    email= models.EmailField(null=True)

    def __str__(self) -> str:
        return self.nombre

