from django.shortcuts import render, redirect
from .models import Departamento, Empleado, Producto
from .forms import DepartamentoForm, EmpleadoForm, ProductoForm


def home(request):
    return render(request, "tienda/index.html")


def crear_departamento(request):
    if request.method == "POST":
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = DepartamentoForm()

    return render(request, "tienda/crear_departamento.html", {"form": form})


def crear_empleado(request):
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = EmpleadoForm()

    return render(request, "tienda/crear_empleado.html", {"form": form})


def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProductoForm()

    return render(request, "tienda/crear_producto.html", {"form": form})

from tienda.models import Departamento

def buscar_departamento(request):
    resultado = None
    if request.GET.get("nombre"):
        nombre = request.GET["nombre"]
        resultado = Departamento.objects.filter(nombre__icontains=nombre)

    return render(request, "tienda/departamentos_tienda.html", {
        "resultado": resultado
    })
