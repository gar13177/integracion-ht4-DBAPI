# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Usuario(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    id_usuario = models.CharField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    fecha_expiracion = models.DateTimeField()

class Orden(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    id_orden = models.CharField(max_length=100, primary_key=True)
    id_usuario = models.ForeignKey(Usuario,db_column='id_usuario', related_name ='ordenes', on_delete=models.CASCADE)

class OrdenDetalle(models.Model):
    fecha_orden = models.DateTimeField()
    id_orden = models.ForeignKey(Orden,db_column='id_orden', related_name ='orden_detalle', on_delete=models.CASCADE)
    id_producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=4)

class Promocion(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_expiracion = models.DateTimeField()
    descripcion = models.CharField(max_length=100)