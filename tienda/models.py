from django.db import models

class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    nro_departamento = models.IntegerField(unique=True)
    nro_empleados = models.IntegerField(null=True)
    fecha_de_creacion = models.DateField(auto_now_add=True)
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
    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre
