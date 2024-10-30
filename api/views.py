from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializer import EstacionesSerializer
from .models import Estaciones
import math
import pdb


class EstacionesViewSet(viewsets.ModelViewSet):
    queryset = Estaciones.objects.all()
    # Crear esa clase
    serializer_class = EstacionesSerializer


class CercanasViewSet(viewsets.ViewSet):
    # Uso este método porque ese me permite hacer una busqueda por Id
    def retrieve(self, request, pk=None):
        # sacar la estación base usando el parámetro pk
        estacion_base = Estaciones.objects.get(id=pk)
        base_lat = estacion_base.ubicacion[0]
        base_long = estacion_base.ubicacion[1]

        # algoritmo: variables para encontrar la estación más cercana
        estacion_mas_cercana = None
        distancia_minima = float('inf')

        for estacion in Estaciones.objects.exclude(id=pk):
            lat = estacion.ubicacion[0]
            long = estacion.ubicacion[1]

            # distancia euclidiana
            distancia = math.sqrt((lat - base_lat) **
                                  2 + (long - base_long) ** 2)

            # Obligo a poner el primer resultado como distancia minima
            if distancia < distancia_minima:
                distancia_minima = distancia
                estacion_mas_cercana = estacion

        # pdb.set_trace()
        # Serializar el resultado
        serializer = EstacionesSerializer(estacion_mas_cercana)
        return Response(serializer.data)
