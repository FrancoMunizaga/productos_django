from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from . import services
from .forms import ProductoForm
from .models import Categoria_Producto, Producto


def home(request):
    categorias = services.obtener_categorias()
    context = {
        'categoria_productos': categorias,
    }
    return render(request, 'home_producto/home.html', context)


def categoria_producto(request, categoria_producto_id: int):
    categoria = Categoria_Producto.objects.filter(pk=categoria_producto_id).first()
    if categoria is None:
        messages.warning(request, 'La categoría indicada no existe.')
        return redirect('home_producto:home')

    termino = request.GET.get('q', '').strip()
    productos = services.productos_de_categoria(categoria, termino)

    context = {
        'categoria_producto': categoria,
        'productos': productos,
        'termino': termino,
    }
    return render(request, 'home_producto/categoria_producto.html', context)


def detalle_producto(request, pk: int):
    producto = Producto.objects.filter(pk=pk).first()
    if producto is None:
        messages.warning(request, 'El producto indicado no existe.')
        return redirect('home_producto:home')

    context = {'producto': producto}
    return render(request, 'home_producto/producto_detalle.html', context)


def crear_producto(request, categoria_producto_id: int):
    categoria = Categoria_Producto.objects.filter(pk=categoria_producto_id).first()
    if categoria is None:
        messages.warning(request, 'La categoría indicada no existe.')
        return redirect('home_producto:home')

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.categoria_producto = categoria
            producto.save()
            messages.success(request, 'Se agregó el producto correctamente.')
            return redirect(reverse('home_producto:detalle_producto', args=[producto.pk]))
    else:
        form = ProductoForm()

    context = {
        'form': form,
        'categoria_producto': categoria,
        'titulo': 'Agregar producto',
    }
    return render(request, 'home_producto/producto_formulario.html', context)


def editar_producto(request, pk: int):
    producto = Producto.objects.filter(pk=pk).first()
    if producto is None:
        messages.warning(request, 'El producto indicado no existe.')
        return redirect('home_producto:home')

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se actualizaron los datos del producto.')
            return redirect(reverse('home_producto:detalle_producto', args=[producto.pk]))
    else:
        form = ProductoForm(instance=producto)

    context = {
        'form': form,
        'categoria_producto': producto.categoria_producto,
        'titulo': 'Editar producto',
        'producto': producto,
    }
    return render(request, 'home_producto/producto_formulario.html', context)


def eliminar_producto(request, pk: int):
    producto = Producto.objects.filter(pk=pk).first()
    if producto is None:
        messages.warning(request, 'El producto indicado no existe.')
        return redirect('home_producto:home')

    if request.method == 'POST':
        categoria_id = producto.categoria_producto.pk
        producto.delete()
        messages.info(request, 'El producto fue eliminado.')
        return redirect(reverse('home_producto:categoria_producto_productos', args=[categoria_id]))

    context = {
        'producto': producto,
    }
    return render(request, 'home_producto/producto_borrar.html', context)
