from django.db import models
import sqlite3

# Create your models here.
class Alumno(models.Model):
    name = models.CharField(max_length=100)
    hours = models.FloatField()

    def __str__(self):
        return f'Nombre: {self.name}, horas: {self.hours}'
