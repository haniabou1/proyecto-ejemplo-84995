from django.urls import path

from .views import (
    home,
    buscar_departamento,
    DepartamentoListView,
    DepartamentoDetailView,
    DepartamentoCreateView,
    DepartamentoUpdateView,
    DepartamentoDeleteView,
)

urlpatterns = [
    path("", home, name="home"),

    path("departamentos/", DepartamentoListView.as_view(), name="departamento_list"),
    path("departamentos/<int:pk>/", DepartamentoDetailView.as_view(), name="departamento_detail"),
    path("departamentos/crear/", DepartamentoCreateView.as_view(), name="departamento_create"),
    path("departamentos/<int:pk>/editar/", DepartamentoUpdateView.as_view(), name="departamento_update"),
    path("departamentos/<int:pk>/borrar/", DepartamentoDeleteView.as_view(), name="departamento_delete"),

    path("buscar-departamento/", buscar_departamento, name="buscar_departamento"),
]
