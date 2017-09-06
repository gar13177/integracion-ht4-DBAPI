# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from dbms.models import *
from dbms.serializers import *
from rest_framework import viewsets
from rest_framework.exceptions import NotFound, ParseError


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        params = dict(self.request.query_params)

        if not len(params):
            return self.queryset

        n_params = dict()
        for key, value in params.items():
            n_params[key] = value[0]
            
        try:
            usuario = Usuario.objects.filter(**n_params)
        except Exception as e:
            raise ParseError(detail=e.message)
    
        if len(usuario) == 0:
            raise NotFound(detail="Usuario with params %s not found"%str(n_params))
        return usuario


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
