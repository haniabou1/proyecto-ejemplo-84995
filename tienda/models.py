from django.db import models


class Departamento(models.Model):
    nombre = models.CharField(max_length=50)                 # CharField #1
    descripcion = models.CharField(max_length=120)           # CharField #2

    nro_departamento = models.IntegerField(unique=True)      # IntegerField unique
    nro_empleados = models.IntegerField(null=True, blank=True)

    fecha_de_creacion = models.DateTimeField(auto_now_add=True)  # DateTimeField
    imagen = models.ImageField(upload_to="departamentos/", null=True, blank=True)  # ImageField

    email_dpto = models.EmailField()

    def __str__(self):
        return self.nombre


class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
