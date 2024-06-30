from django.db import models

# Create your tests here.

# tabla navbar
class Nav(models.Model):
    id_nav = models.AutoField(db_column='id_Nav', primary_key=True)
    nombre_nav = models.CharField(max_length=20, blank=False, null=False)


# tabla servicios
class Servicio(models.Model):
    id_servicio = models.AutoField(db_column='idServicios', primary_key=True)
    titulo_servicio = models.CharField(max_length=50, blank=False, null=False)
    descripcion_servicio = models.CharField(max_length=1000, blank=False, null=False)
    precio = models.CharField(max_length=45)

    def __str__(self):
        return str(self.titulo_servicio)
        