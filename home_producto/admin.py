from django.contrib import admin
from .models import Categoria_Producto

@admin.register(Categoria_Producto)
class Categoria_ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)
