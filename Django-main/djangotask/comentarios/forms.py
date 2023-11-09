from django import forms
from .models import Comentarios

class ComentariosForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ['nombre', 'email', 'comentario']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'comentario': forms.Textarea(attrs={'class':'form-control'}),
        }