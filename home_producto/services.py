from .models import Categoria_Producto

def obtener_categorias():
    return Categoria_Producto.objects.all()

def productos_de_categoria(categoria, termino=''):
    lista = categoria.productos.all()
    if termino:
        lista = lista.filter(nombre__icontains=termino)
    return lista