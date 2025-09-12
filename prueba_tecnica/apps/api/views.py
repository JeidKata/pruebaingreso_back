from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from prueba_tecnica.apps.datos.municipios.models import Municipio
from prueba_tecnica.apps.datos.oficinas.models import Oficina
from .serializers.municipio_serialize import MunicipioSerializer, MunicipioGeoSerializer

class MunicipiosPorDepartamentoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, departamento):
        municipios = Municipio.objects.filter(dpto__iexact=departamento)
        serializer = MunicipioSerializer(municipios, many=True)
        return Response(serializer.data)

class GeometriaMunicipioPorOficinaView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, oficina_id):
        try:
            oficina = Oficina.objects.get(pk=oficina_id)
            municipio = Municipio.objects.get(municipio__iexact=oficina.municipio)
            serializer = MunicipioGeoSerializer(municipio)
            return Response(serializer.data)
        except (Oficina.DoesNotExist, Municipio.DoesNotExist):
            return Response({'error': 'Oficina o municipio no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        