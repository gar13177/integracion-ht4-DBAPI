from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from dbms.views import *
from res_framework import renderers

usuario_list = UsuarioViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
usuario_detail = UsuarioViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

orden_list = OrdenViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
orden_detail = OrdenViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
ordendetalle_list = OrdenDetalleViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
ordendetalle_detail = OrdenDetalleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

promocion_list = PromocionViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
promocion_detail = PromocionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^orden/$', orden_list, name='orden-list'),
    url(r'^orden/(?P<pk>[0-9]+)/$', orden_detail, name='orden-detail'),
    url(r'^orden/detalle$', ordendetalle_list, name='ordendetalle-list'),
    url(r'^orden/detalle(?P<pk>[0-9]+)/$', ordendetalle_detail, name='ordendetalle-detail'),
    url(r'^usuario/$', usuario_list, name='usuario-list'),
    url(r'^usuario/(?P<pk>[0-9]+)/$', usuario_detail, name='usuario-detail'),
    url(r'^promocion/$', promocion_list, name='promocion-list'),
    url(r'^promocion/(?P<pk>[0-9]+)/$', usuario_detail, name='promocion-detail'),
])
