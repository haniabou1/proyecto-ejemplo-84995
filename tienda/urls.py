from django.urls import path
from .views import home, listar_departamentos

urlpatterns = [
    path("", home, name="home"),
    path("lista_departamentos/", listar_departamentos, name="departament_list"),
]
