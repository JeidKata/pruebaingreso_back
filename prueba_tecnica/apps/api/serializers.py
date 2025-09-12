from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from prueba_tecnica.apps.datos.municipios.models import Municipio
from prueba_tecnica.apps.datos.oficinas.models import Oficina

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'

class MunicipioGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Municipio
        geo_field = "geom"
        fields = ('id', 'municipio', 'geom')

class OficinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oficina
        fields = '__all__'
        