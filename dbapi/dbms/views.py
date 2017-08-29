# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from dbms.models import *
from dbms.serializers import *
from rest_framework import viewsets


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

    def perform_create(self, serializer):
        serializer.save(id_usuario=Usuario.objects.get(id_usuario=str(self.request.data['id_usuario'][0])))

class OrdenDetalleViewSet(viewsets.ModelViewSet):
    queryset = OrdenDetalle.objects.all()
    serializer_class = OrdenDetalleSerializer

    def perform_create(self, serializer):
        serializer.save(id_orden=Orden.objects.get(id_orden=str(self.request.data['id_orden'][0])))

class PromocionViewSet(viewsets.ModelViewSet):
    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer