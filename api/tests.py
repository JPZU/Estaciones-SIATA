from django.test import TestCase
from api.models import Estaciones
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from api.serializer import EstacionesSerializer

# Create your tests here.


class EstacionesViewSetTest(TestCase):
    def setUp(self):
        self.estacion = Estaciones.objects.create(
            nombre="Estación Principal",
            ubicacion=[-1, 1]  # almacena un json
        )
        self.prueba = APIClient()

    def test_list_should_return_200(self):
        url = reverse(
            # django me genera automaticamente el basename='estaciones-detail'
            "estaciones-detail",
            kwargs={"pk": self.estacion.id}
        )
        response = self.prueba.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CercanasViewSetTest(TestCase):
    def setUp(self):
        # Crear varias estaciones con ubicaciones diferentes
        self.estacion_base = Estaciones.objects.create(
            nombre="Estación Base",
            ubicacion=[0, 0]
        )
        self.estacion_cercana = Estaciones.objects.create(
            nombre="Estación Cercana",
            ubicacion=[1, 1]
        )
        self.estacion_lejana = Estaciones.objects.create(
            nombre="Estación Lejana",
            ubicacion=[10, 10]
        )
        self.prueba = APIClient()

    def test_retrieve_cercana(self):
        # obtener la URL para la estación cercana
        url = reverse("cercanas-retrieve",
                      kwargs={"id": self.estacion_base.id}
                      )

        response = self.prueba.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificar que la estación mas cercana este correcta
        estacion_cercana_serializada = EstacionesSerializer(
            self.estacion_cercana)

        self.assertEqual(response.data, estacion_cercana_serializada.data)
