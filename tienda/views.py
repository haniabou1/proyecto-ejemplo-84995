from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Departamento
from pages.models import Page


def home(request):
    paginas_inicio = Page.objects.all().order_by("id")[:4]
    return render(request, "tienda/index.html", {"paginas_inicio": paginas_inicio})


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "tienda/departamento_list.html"
    context_object_name = "departamentos"

    def get_queryset(self):
        qs = super().get_queryset().order_by("nombre")
        q = self.request.GET.get("q", "").strip()
        if q:
            qs = qs.filter(
                Q(nombre__icontains=q)
                | Q(descripcion__icontains=q)
                | Q(nro_departamento__icontains=q)
            )
        return qs


class DepartamentoDetailView(DetailView):
    model = Departamento
    template_name = "tienda/departamento_detail.html"
    context_object_name = "departamento"


class DepartamentoCreateView(LoginRequiredMixin, CreateView):
    model = Departamento
    fields = ["nombre", "descripcion", "nro_departamento", "email_dpto", "nro_empleados", "imagen"]
    template_name = "tienda/departamento_form.html"
    success_url = reverse_lazy("departamento_list")


class DepartamentoUpdateView(LoginRequiredMixin, UpdateView):
    model = Departamento
    fields = ["nombre", "descripcion", "nro_departamento", "email_dpto", "nro_empleados", "imagen"]
    template_name = "tienda/departamento_form.html"
    success_url = reverse_lazy("departamento_list")


class DepartamentoDeleteView(LoginRequiredMixin, DeleteView):
    model = Departamento
    template_name = "tienda/departamento_confirm_delete.html"
    success_url = reverse_lazy("departamento_list")


@login_required
def buscar_departamento(request):
    """
    Buscador simple (FBV) con decorador para cumplir requisito.
    """
    q = request.GET.get("nombre", "").strip()

    resultado = Departamento.objects.none()
    if q:
        resultado = Departamento.objects.filter(nombre__icontains=q).order_by("nombre")

    return render(request, "tienda/departamentos_tienda.html", {
        "resultado": resultado,
        "q": q,
    })
