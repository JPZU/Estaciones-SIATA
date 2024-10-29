from rest_framework import viewsets
from .serializer import EstacionesSerializer
from .models import Estaciones

# Create your views here.


class EstacionesViewSet(viewsets.ModelViewSet):
    queryset = Estaciones.objects.all()
    # Crear esa clase
    serializer_class = EstacionesSerializer
