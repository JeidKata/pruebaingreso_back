from django.contrib.gis.db import models

# Create your models here.
class Municipio(models.Model):
    gid = models.AutoField(primary_key=True)
    cod_dane = models.CharField(max_length=255)
    dpto = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    disposicio = models.CharField(max_length=255)
    aÑo_creac = models.CharField(max_length=255)
    geom = models.MultiPolygonField(srid=4326)  # O PolygonField si tu shapefile es de polígonos simples

    class Meta:
        managed = False  # Django no gestionará la tabla
        db_table = 'municipios'