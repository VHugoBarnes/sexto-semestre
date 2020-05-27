# coding: utf-8


from __future__ import unicode_literals
from django.db import models


class DatosPersonales(models.Model):

    numero_control = models.CharField(max_length=10, primary_key=True)
    apellido_paterno = models.CharField(max_length=35)
    apellido_materno = models.CharField(max_length=35)
    nombre = models.CharField(max_length=35)
    curp = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    sexos = (('F', 'Femenino'), ('M', 'Masculino'))
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    #foto = models.ImageField(upload_to='photos')

