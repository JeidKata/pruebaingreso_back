from rest_framework import serializers
from apps.datos.oficinas.models import Oficina

class OficinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oficina
        fields = '__all__'
