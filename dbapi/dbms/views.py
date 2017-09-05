# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import django_filters.rest_framework
from django.shortcuts import get_object_or_404
from django.http import Http404
from dbms.models import *
from dbms.serializers import *
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from dbms.serializers import UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        params = self.request.query_params
        data = Usuario.objects.all()
        if 'nombre' in params:
            data = get_object_or_404(Usuario, nombre=params['nombre'])
            if not (isinstance(data, Usuario)):
                return Response("No se encontró", status=status.HTTP_404_NOT_FOUND)
            data = [data]

        if 'contrasena' in params:
            data = get_object_or_404(Usuario, nombre=params['nombre'], contrasena=params['contrasena'])
            if not (isinstance(data, Usuario)):
                return Response("No se encontró", status=status.HTTP_404_NOT_FOUND)
            data = [data]

        return data


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
