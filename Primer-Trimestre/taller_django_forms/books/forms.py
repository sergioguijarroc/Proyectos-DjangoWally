from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'resume','rating']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Textarea(attrs={'class': 'form-control'}),
            'resume': forms.Textarea(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(),
        }