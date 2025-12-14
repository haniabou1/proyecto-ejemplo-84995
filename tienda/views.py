from django.shortcuts import render
from tienda.models import Departamento

def home(request):
    return render(request, "tienda/index.html")


def listar_departamentos(request):
    Departamentos_query = Departamento.objects.all()
    contexto = {
        "departamentos": Departamentos_query
    }
    return render(request, "tienda/departamentos_tienda.html", contexto)

