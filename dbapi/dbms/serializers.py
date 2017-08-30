from rest_framework import serializers
from dbms.models import *
from django.contrib.auth.models import User

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    ordenes = serializers.HyperlinkedRelatedField(many=True, view_name='orden-detail', read_only=True)
    class Meta:
        model = Usuario
        fields =  ('fecha_creacion', 'id_usuario', 'fecha_expiracion','ordenes', 'nombre', 'contrasena')

class OrdenSerializer(serializers.HyperlinkedModelSerializer):
    id_usuario = serializers.CharField(source='id_usuario.id_usuario')
    orden_detalle = serializers.HyperlinkedRelatedField(many=True, view_name='ordendetalle-detail', read_only=True)
    class Meta:
        model = Orden
        fields = ('fecha_creacion','id_orden','id_usuario','orden_detalle')

class OrdenDetalleSerializer(serializers.HyperlinkedModelSerializer):
    id_orden = serializers.CharField(source='id_orden.id_orden')
    class Meta:
        model = OrdenDetalle
        fields = ('fecha_orden','id_orden','id_producto','cantidad','precio_unitario')

class PromocionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Promocion 
        fields = ('fecha_creacion','fecha_expiracion','descripcion')
