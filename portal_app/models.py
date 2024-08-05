from django.db import models

# Create your models here.
class TipoUsuario(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    tipo_usuario = models.CharField(max_length=50, null=False)

    class Meta:
        managed=False
        db_table='tipo_usuarios'

    def __str__(self):
        return self.tipo_usuario

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    comuna = models.CharField(max_length=50, null=False)

    class Meta:
        managed = False
        db_table='comunas'

    def __str__(self):
        return self.comuna

class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    region = models.CharField(max_length=50, null=False)

    class Meta:
        managed=False
        db_table='regiones'

    def __str__(self):
        return self.region

class TipoInmueble(models.Model):
    id_tipo_inmueble = models.AutoField(primary_key=True)
    tipo_inmueble = models.CharField(max_length=50, null=False)

    class Meta:
        managed=False
        db_table='tipo_inmuebles'

    def __str__(self):
        return self.tipo_inmueble

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    rut = models.CharField(max_length=12, null=False, unique=True)
    direccion = models.CharField(max_length=100, null=False)
    telefono = models.CharField(max_length=20, null=False)
    correo = models.EmailField(unique=True, null=False)
    id_tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, db_column='id_tipo_usuario')

    class Meta:
        managed = False
        db_table = 'usuarios'

    def __str__(self):
        return self.nombre

class Inmueble(models.Model):
    id_inmueble = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60, null=False)
    m2_construidos = models.FloatField(null=False)
    m2_terreno = models.FloatField(null=False)
    nro_estacionamiento = models.IntegerField()
    nro_habitaciones = models.IntegerField()
    nro_banio = models.IntegerField()
    direccion = models.CharField(max_length=100, null=False)
    precio_arriendo = models.FloatField(null=False)
    id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE, db_column='id_usuario')
    id_comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE, db_column='id_comuna')
    id_region = models.ForeignKey(Region,on_delete=models.CASCADE, db_column='id_region')
    id_tipo_inmueble = models.ForeignKey(TipoInmueble,on_delete=models.CASCADE,db_column='id_tipo_inmueble')

    class Meta:
        managed = False
        db_table = 'inmuebles'

    def __str__(self):
        return self.nombre







