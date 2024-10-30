from django.db import models

# Creo mi entidad


class Estaciones(models.Model):
    # Garantiza que los numeros sean de 1 a 99.........
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    ubicacion = models.JSONField()  # almacena un json
    # Constructor para cuando haga referencia a el me traiga el nombre

    def __str__(self):
        return f"{self.nombre} - {self.ubicaion}"
