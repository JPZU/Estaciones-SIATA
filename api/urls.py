from django.urls import path, include
from rest_framework import routers
from api import views

# Me permite manejar multipes rutas CRUD
router = routers.DefaultRouter()
# La 'r' es importante para que el enteinde que puede tener '/'
router.register(r'estaciones', views.EstacionesViewSet)
router.register(r'estaciones/cercanas',
                views.CercanasViewSet, basename="cercanas")

urlpatterns = [
    path('', include(router.urls)),
    path('estaciones/cercanas/<int:id>/', views.CercanasViewSet.as_view(
        {'get': 'retrieve'}), name='cercanas-retrieve'),
]
