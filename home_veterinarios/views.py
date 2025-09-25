from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from . import services
from .forms import VeterinarioForm
from .models import Categoria, Veterinario

def home(request):
    categorias = services.obtener_categorias()
    context = {
        'categorias': categorias,
    }
    return render(request, 'home_veterinarios/home.html', context)

def categoria_veterinarios(request, categoria_id: int):
    categoria = Categoria.objects.filter(pk=categoria_id).first()
    if categoria is None:
        messages.warning(request, 'La categoría indicada no existe.')
        return redirect('home_veterinarios:home')

    termino = request.GET.get('q', '').strip()
    veterinarios = services.veterinarios_de_categoria(categoria, termino)

    context = {
        'categoria': categoria,
        'veterinarios': veterinarios,
        'termino': termino,
    }
    return render(request, 'home_veterinarios/categoria.html', context)


def detalle_veterinario(request, pk: int):
    veterinario = Veterinario.objects.filter(pk=pk).first()
    if veterinario is None:
        messages.warning(request, 'El veterinario indicado no existe.')
        return redirect('home_veterinarios:home')
    return render(request, 'home_veterinarios/veterinario_detalle.html', {'veterinario': veterinario})


def crear_veterinario(request, categoria_id: int):
    categoria = Categoria.objects.filter(pk=categoria_id).first()
    if categoria is None:
        messages.warning(request, 'La categoría indicada no existe.')
        return redirect('home_veterinarios:home')

    if request.method == 'POST':
        form = VeterinarioForm(request.POST, request.FILES)
        if form.is_valid():
            veterinario = form.save(commit=False)
            veterinario.categoria = categoria
            veterinario.save()
            messages.success(request, 'Se agregó el veterinario correctamente.')
            return redirect(reverse('home_veterinarios:detalle_veterinario', args=[veterinario.pk]))
    else:
        form = VeterinarioForm()

    context = {
        'form': form,
        'categoria': categoria,
        'titulo': 'Agregar veterinario',
    }
    return render(request, 'home_veterinarios/veterinario_formulario.html', context)


def editar_veterinario(request, pk: int):
    veterinario = Veterinario.objects.filter(pk=pk).first()
    if veterinario is None:
        messages.warning(request, 'El veterinario indicado no existe.')
        return redirect('home_veterinarios:home')

    if request.method == 'POST':
        form = VeterinarioForm(request.POST, request.FILES, instance=veterinario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se actualizaron los datos del veterinario.')
            return redirect(reverse('home_veterinarios:detalle_veterinario', args=[veterinario.pk]))
    else:
        form = VeterinarioForm(instance=veterinario)

    context = {
        'form': form,
        'categoria': veterinario.categoria,
        'titulo': 'Editar veterinario',
        'veterinario': veterinario,
    }
    return render(request, 'home_veterinarios/veterinario_formulario.html', context)


def eliminar_veterinario(request, pk: int):
    veterinario = Veterinario.objects.filter(pk=pk).first()
    if veterinario is None:
        messages.warning(request, 'El veterinario indicado no existe.')
        return redirect('home_veterinarios:home')

    if request.method == 'POST':
        categoria_id = veterinario.categoria.pk
        veterinario.delete()
        messages.info(request, 'El veterinario fue eliminado.')
        return redirect(reverse('home_veterinarios:categoria_veterinarios', args=[categoria_id]))

    context = {
        'veterinario': veterinario,
    }
    return render(request, 'home_veterinarios/veterinario_borrar.html', context)
