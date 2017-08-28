from django.conf.urls import url, include
from dbms import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'orden', views.OrdenViewSet)
router.register(r'ordendetalle', views.OrdenDetalleViewSet)
router.register(r'promocion', views.PromocionViewSet)
router.register(r'usuario', views.UsuarioViewSet)


schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]