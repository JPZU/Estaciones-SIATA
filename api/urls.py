from django.urls import path, include
from rest_framework import routers
from api import views

# Me permite manejar multipes rutas CRUD
router = routers.DefaultRouter()
# La 'r' es importante para que el enteinde que puede tener '/'
router.register(r'estaciones', views.EstacionesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
