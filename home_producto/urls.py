from django.urls import path
from . import views

app_name = 'home_producto'
urlpatterns = [
    path('', views.home, name='home'),
    path('categorias_producto/<int:categoria_producto_id>/', views.categoria_producto, name='categoria_producto'),
    path('categorias_producto/<int:categoria_procuto_id>/producto/nuevo/', views.crear_producto, name='crear_productos'),
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('producto/<int:pk>/editar/', views.editar_producto, name='editar_producto '),
    path('producto/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto '),
]
