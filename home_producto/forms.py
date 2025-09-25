from django import forms

from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','sku','descripcion', 'foto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'sku': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123456789'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'foto': 'Sube una imagen desde tu computador (opcional).',
        }
