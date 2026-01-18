from django import forms
from .models import Departamento, Empleado, Producto


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = [
            "nombre",
            "descripcion",
            "nro_departamento",
            "email_dpto",
            "nro_empleados",
            "imagen",
        ]
        labels = {
            "nombre": "Nombre del departamento",
            "descripcion": "Descripción",
            "nro_departamento": "Número de departamento",
            "email_dpto": "Email del departamento",
            "nro_empleados": "Cantidad de empleados",
            "imagen": "Imagen",
        }


class EmpleadoForm(forms.ModelForm):
    departamento = forms.ModelChoiceField(
        queryset=Departamento.objects.all(),
        empty_label="Seleccione un departamento"
    )

    class Meta:
        model = Empleado
        fields = ["nombre", "apellido", "departamento"]
        labels = {
            "nombre": "Nombre",
            "apellido": "Apellido",
            "departamento": "Departamento",
        }


class ProductoForm(forms.ModelForm):
    departamento = forms.ModelChoiceField(
        queryset=Departamento.objects.all(),
        empty_label="Seleccione un departamento"
    )

    class Meta:
        model = Producto
        fields = ["nombre", "precio", "departamento"]
        labels = {
            "nombre": "Nombre del producto",
            "precio": "Precio",
            "departamento": "Departamento",
        }
