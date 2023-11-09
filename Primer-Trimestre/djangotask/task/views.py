from django.shortcuts import render,redirect
from .models import Task
'''
Importar formulario
'''
from .forms import TaskForm
def task(request):
    tasks = Task.objects.all()
    '''
    if=Si el formulario está para enviarlo con el metodo post 
    else=Si el formulario es nuevo se crea otro formulario vacío
    '''
    if request.method== 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            '''
            Redirect confirmacion nuevo formulario ir a la vista de confirmacion
            '''
            return redirect('task')
    else:
        form=TaskForm()
    return render(request, 'task/task.html', {'tasks': tasks,'form':form})
# Create your views here.
