from django.urls import path
from .views import MunicipiosPorDepartamentoView, GeometriaMunicipioPorOficinaView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('municipios-por-departamento/<str:departamento>/', MunicipiosPorDepartamentoView.as_view(), name='municipios-por-departamento'),
    path('geometria-municipio-por-oficina/<int:oficina_id>/', GeometriaMunicipioPorOficinaView.as_view(), name='geometria-municipio-por-oficina'),

]
