from django.shortcuts import render,redirect
from .models import Task
from django.http import HttpResponseRedirect
from django.views import View

'''
Importar formulario
'''
from .forms import TaskForm
'''def task(request):
    tasks = Task.objects.all()
    
    if=Si el formulario está para enviarlo con el metodo post 
    else=Si el formulario es nuevo se crea otro formulario vacío
    
    if request.method== 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            
            Redirect confirmacion nuevo formulario ir a la vista de confirmacion
            
            return redirect('task')
    else:
        form=TaskForm()
    return render(request, 'task/task.html', {'tasks': tasks,'form':form})

'''

class MyView(View):
    tasks=Task.objects.all()
    template_name='task/list_tasks.html'
    def get(self, request):
        form=TaskForm()
        return render(request,self.template_name, {'tasks':self.actualizaTask(),'form': form})
    def post(self,request):
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task')
        return render(request,self.template_name,{'tasks':self.actualizaTask(),'form': form})
    def actualizaTask(self):
        self.tasks=Task.objects.all()
# Create your views here.
