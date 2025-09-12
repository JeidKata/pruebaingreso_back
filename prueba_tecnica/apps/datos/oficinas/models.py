'''
    Models for the Oficina entity.
'''
from django.contrib.gis.db import models

class Oficina(models.Model):
    gid = models.AutoField(primary_key=True)
    # __gid = models.FloatField() # Django no permite campos que comiencen con __
    nombre = models.CharField(max_length=255)
    departamen = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    geom = models.PointField(srid=4326)  # O MultiPointField si tu shapefile es multipunto

    class Meta:
        managed = False
        db_table = 'oficinas'