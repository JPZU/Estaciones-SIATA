from django.urls import path, include
from rest_framework import routers
from api import views

# inicializar el router para manejar multiples rutas CRUD
router = routers.DefaultRouter()
# registrar el ViewSet para estaciones con rutas CRUD estandar
router.register(r'estaciones', views.EstacionesViewSet, basename="estaciones")

# registrar el viewSet para estaciones cercanas con un basename personalizado
router.register(r'estaciones/cercanas',
                views.CercanasViewSet, basename="cercanas")

urlpatterns = [
    # incluir todas las rutas generadas por el router
    path('', include(router.urls)),
    path('estaciones/cercanas/<int:id>/', views.CercanasViewSet.as_view(
        {'get': 'retrieve'}), name='cercanas-retrieve'),
]
