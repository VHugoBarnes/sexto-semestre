# coding: utf-8


from __future__ import unicode_literals
from django.db import models


class Alumno(models.Model):

    apellido_paterno = models.CharField(max_length=35)
    apellido_materno = models.CharField(max_length=35)
    nombre = models.CharField(max_length=35)
    dni = models.CharField(max_length=8)
    fecha_nacimiento = models.DateField()
    sexos = (('F', 'Femenino'), ('M', 'Masculino'))
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    foto = models.ImageField(upload_to='photos')

    def nombre_completo(self):
        cadena = "{0} {1} {2}"
        return cadena.format(self.apellido_paterno, self.apellido_materno, self.nombre)

    def __str__(self):
        return self.nombre_completo()


class Curso(models.Model):

    nombre = models.CharField(max_length=30)
    estado = models.BooleanField(default=True)
    creditos = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return "{0} -> {1}".format(self.nombre, self.creditos)

    
class Matricula(models.Model):

    alumno = models.ForeignKey(Alumno, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fecha_matricula = models.DateTimeField(auto_now=True)

    def __str__(self):
        cadena = "{0} inscrito en: {1}"
        return cadena.format(self.alumno, self.curso)

