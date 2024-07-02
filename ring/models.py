from django.db import models

# Create your models here.

class Nav(models.Model):
    id_nav = models.AutoField(db_column='idNav', primary_key=True)
    nombre_nav = models.CharField(max_length=20, blank=False, null=False)
    url_nav = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.nombre_nav)

    class Meta:
        db_table = 'Navs'

class Quienesomo(models.Model):
    id_quienesomos = models.AutoField(db_column='idQuienesomos', primary_key=True)
    titulo_quienesomos = models.CharField(max_length=50, blank=False, null=False)
    descripcion_quienesomos = models.CharField(max_length=1000, blank=False, null=False)

    def __str__(self):
        return str(self.titulo_quienesomos)

    class Meta:
        db_table = 'Quienes_somos'

class Servicio(models.Model):
    id_servicio = models.AutoField(db_column='idServicios', primary_key=True)
    titulo_servicio = models.CharField(max_length=50, blank=False, null=False)
    descripcion_servicio = models.CharField(max_length=1000, blank=False, null=False)

    def __str__(self):
        return str(self.titulo_servicio)

    class Meta:
        db_table = 'Servicio'