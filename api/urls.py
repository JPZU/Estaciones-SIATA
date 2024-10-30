from django.urls import path, include
from rest_framework import routers
from api import views

# Inicializar el router para manejar múltiples rutas CRUD
router = routers.DefaultRouter()

# Registrar el ViewSet para estaciones con rutas CRUD estándar
router.register(r'estaciones', views.EstacionesViewSet, basename="estaciones")

# Registrar el ViewSet para estaciones cercanas con un nombre base personalizado
router.register(r'estaciones/cercanas',
                views.CercanasViewSet, basename="cercanas")

urlpatterns = [
    # Incluir todas las rutas generadas por el router
    path('', include(router.urls)),
    # Ruta personalizada para obtener la estación más cercana a una estación dada, anidada dentro de estaciones
    path('estaciones/cercanas/<int:id>/', views.CercanasViewSet.as_view(
        {'get': 'retrieve'}), name='cercanas-retrieve'),
]
