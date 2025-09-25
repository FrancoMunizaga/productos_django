from django.urls import path
from . import views

app_name = 'home_veterinarios'
urlpatterns = [
    path('', views.home, name='home'),
    path('categorias/<int:categoria_id>/', views.categoria_veterinarios, name='categoria_veterinarios'),
    path('categorias/<int:categoria_id>/veterinarios/nuevo/', views.crear_veterinario, name='crear_veterinario'),
    path('veterinarios/<int:pk>/', views.detalle_veterinario, name='detalle_veterinario'),
    path('veterinarios/<int:pk>/editar/', views.editar_veterinario, name='editar_veterinario'),
    path('veterinarios/<int:pk>/eliminar/', views.eliminar_veterinario, name='eliminar_veterinario'),
]
