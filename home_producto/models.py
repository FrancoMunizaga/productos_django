from django.db import models


class Categoria_Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='categorias/', blank=True, null=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self) -> str:
        return self.nombre


class Producto(models.Model):
    categoria = models.ForeignKey('Categoria_Producto', related_name='productos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=120)
    sku = models.CharField(max_length=12)
    descripcion = models.TextField(blank=True)
    foto = models.ImageField(upload_to='productos/', blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self) -> str:
        return f"{self.nombre} ({self.categoria.nombre})"
