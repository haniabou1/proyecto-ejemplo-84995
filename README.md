# Proyecto_Final_HaniAbouSaada

La aplicación simula una **tienda por departamentos**, similar a una tienda tipo Walmart, desarrollada con **Django**.  
Permite gestionar departamentos, empleados y productos, además de mostrar **páginas informativas dinámicas** accesibles desde la página de inicio.

---

## Funcionalidades principales

- Página de inicio con mensaje de bienvenida.
- Barra de navegación (NavBar).
- Visualización de **páginas informativas** creadas desde el panel de administración:
  - Quiénes somos
  - Contacto y ayuda
  - Políticas
  - Información general
- Gestión completa de **Departamentos** (crear, listar, editar y eliminar).
- Asociación de **Empleados** a un departamento.
- Asociación de **Productos** a un departamento.
- Buscador de departamentos por nombre.
- Sistema de **autenticación de usuarios**:
  - Registro
  - Login
  - Logout
  - Perfil de usuario con avatar y biografía
- Restricción de acciones (crear, editar y borrar) solo para usuarios autenticados.
- Uso de **herencia de plantillas HTML**.
- Uso de **vistas basadas en clases (CBV)** y **vistas basadas en funciones (FBV)**.
- Base de datos **SQLite** (excluida del repositorio).

---

## Modelos creados

### Departamento
- nombre
- descripcion
- nro_departamento (único)
- nro_empleados
- email_dpto
- imagen

### Empleado
- nombre
- apellido
- departamento (ForeignKey)

### Producto
- nombre
- precio
- departamento (ForeignKey)

### Page (páginas informativas)
- title
- slug
- content
- created
- updated

---

## Estructura del proyecto

Proyecto_Final/  
│  
├── manage.py  
├── Proyecto_Final_Abousaada/  
│ ├── settings.py  
│ ├── urls.py  
│ └── wsgi.py  
│  
├── tienda/  
│ ├── models.py  
│ ├── views.py  
│ ├── urls.py  
│ └── templates/tienda/  
│  
├── pages/  
│ ├── models.py  
│ ├── views.py  
│ ├── urls.py  
│ └── templates/pages/  
│  
├── accounts/  
│ ├── models.py  
│ ├── views.py  
│ ├── urls.py  
│ └── templates/accounts/  
│  
└── templates/  
    └── base.html  

---

## Panel de administración

Desde el **admin de Django** se pueden:

- Crear y editar páginas informativas.
- Gestionar usuarios y perfiles.
- Administrar departamentos, empleados y productos.

---

## Tecnologías utilizadas

- Python 3
- Django 5
- SQLite
- HTML y CSS
- Django Admin

---

## Autor

**Hani Abou Saada**  
Proyecto Final – Curso Python (CoderHouse)
