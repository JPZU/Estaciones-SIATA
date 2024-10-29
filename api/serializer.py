from rest_framework import serializers
from .models import Estaciones


class EstacionesSerializer(serializers.ModelSerializer):
    class Meta:
        # modelos
        model = Estaciones
        # campos que quiero serializar
        fields = "__all__"  # Que se serialicen todos los campos del modelo
