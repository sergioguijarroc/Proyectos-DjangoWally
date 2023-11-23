import netrc
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from .models import Book
from django.views import View
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from django.forms import formset_factory
from .forms import BookForm

class List_book(ListView):
    model = Book
    
class Book_num(DetailView):
    model=Book


class Update_book(UpdateView):
    model=Book
    fields=['title','author','rating','resume']
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("list")
class Delete_book(DeleteView):
    model=Book
    success_url = reverse_lazy("list")
class Create_book(CreateView):
    model=Book
    fields="__all__"
    success_url = reverse_lazy("list")
    queryset = 


    

# Create your views here.