from django.db import models
from ckeditor.fields import RichTextField


class Page(models.Model):
    title = models.CharField(
        'Título',
        max_length=200
    )

    slug = models.SlugField(
        unique=True,
        help_text='Se usa en la URL. Ej: contacto, quienes-somos'
    )

    content = RichTextField('Contenido')

    # Navegación
    show_in_menu = models.BooleanField('Mostrar en menú', default=True)
    order = models.PositiveIntegerField('Orden', default=0)

    # SEO
    meta_title = models.CharField(
        'Meta título',
        max_length=60,
        blank=True
    )
    meta_description = models.CharField(
        'Meta descripción',
        max_length=160,
        blank=True
    )

    # Estado
    is_home = models.BooleanField('Es página principal', default=False)
    is_active = models.BooleanField('Activa', default=True)

    created = models.DateTimeField('Creada', auto_now_add=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'

    def __str__(self):
        return self.title
