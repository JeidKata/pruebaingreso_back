from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from prueba_tecnica.apps.datos.municipios.models import Municipio

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'


class MunicipioGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Municipio
        geo_field = "geom"
        fields = ('id', 'municipio', 'geom')
        