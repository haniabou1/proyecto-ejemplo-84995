# TP3_HaniAbousaada

La aplicación simula una web sencilla de gestión de una tienda, permitiendo crear departamentos, empleados y productos, y realizar búsquedas en la base de datos.

---

## Funcionalidades principales

- Página de inicio.
- Creación de **Departamentos**.
- Creación de **Empleados**, asociados a un departamento.
- Creación de **Productos**, asociados a un departamento.
- Búsqueda de departamentos por nombre.
- Uso de **herencia de plantillas HTML**.
- Formularios creados con **ModelForms**.
- Base de datos SQLite.

---

## Modelos creados

El proyecto cuenta con **3 modelos**:

- **Departamento**
  - nombre
  - nro_departamento
  - nro_empleados
  - email_dpto
  - fecha_de_creacion

- **Empleado**
  - nombre
  - apellido
  - departamento (ForeignKey)

- **Producto**
  - nombre
  - precio
  - departamento (ForeignKey)

---

## Estructura del proyecto

- Proyecto: `TP3_HaniAbousaada`
- Aplicación: `tienda`
- Templates: `tienda/templates/tienda/`
- Base de datos: `db.sqlite3`