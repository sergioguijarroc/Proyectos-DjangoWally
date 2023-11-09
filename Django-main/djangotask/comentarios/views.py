from .forms import ComentariosForm
from django.shortcuts import render,redirect
from .models import Comentarios
'''
Importar formulario
'''

def comentarios(request):
    comentarios = Comentarios.objects.all()
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
            return redirect('confirmacion')
    else:
        form=ComentariosForm()
    return render(request, 'comentarios/base.html', {'comentarios': comentarios,'form':form})
# Create your views here.
def confirmacion(request):
    return render(request,'comentarios/confirmacion.html')
