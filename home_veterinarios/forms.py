from django import forms

from .models import Veterinario

class VeterinarioForm(forms.ModelForm):
    class Meta:
        model = Veterinario
        fields = ['nombre', 'rut', 'correo', 'descripcion', 'foto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '12345678-9'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'foto': 'Sube una imagen desde tu computador (opcional).',
        }
