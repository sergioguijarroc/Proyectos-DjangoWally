from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ComentariosForm
from .models import Comentarios
'''
Importar formulario
'''

def formulario(request):
    '''
    if=Si el formulario está para enviarlo con el metodo post 
    else=Si el formulario es nuevo se crea otro formulario vacío
    '''
    if request.method== 'POST':
        form=ComentariosForm(request.POST)
        if form.is_valid():
            form.save()
            '''
            Redirect confirmacion nuevo formulario ir a la vista de confirmacion
            '''
            print("Redirigiendo a la página de confirmación...")
            return redirect('confirmacion')
    else:
        form=ComentariosForm()
    return render(request, 'comentarios/base.html', {'form':form})
# Create your views here.

def confirmacion(request):
    mensaje="Gracias por tu comentario"
    return render(request,'comentarios/confirmacion.html',{'mensaje':mensaje})
def lista_comentarios(request):
    lista= Comentarios.objects.all()
    return render(request,'comentarios/lista_comentarios.html',{'lista':lista})