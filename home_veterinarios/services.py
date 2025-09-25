from .models import Categoria

def obtener_categorias():
    return Categoria.objects.all()

def veterinarios_de_categoria(categoria, termino=''):
    lista = categoria.veterinarios.all()
    if termino:
        lista = lista.filter(nombre__icontains=termino)
    return lista