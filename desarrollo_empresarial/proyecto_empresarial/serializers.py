from rest_framework import serializers
from proyecto_empresarial.models import EtapaProyecto

class EtapaProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EtapaProyecto
        fields = '__all__'
        