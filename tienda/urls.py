from django.urls import path
from .views import (
    home,
    crear_departamento,
    crear_empleado,
    crear_producto,
    buscar_departamento,
)

urlpatterns = [
    path("", home, name="home"),
    path("crear-departamento/", crear_departamento, name="crear_departamento"),
    path("crear-empleado/", crear_empleado, name="crear_empleado"),
    path("crear-producto/", crear_producto, name="crear_producto"),
    path("buscar-departamento/", buscar_departamento, name="buscar_departamento"),
]
