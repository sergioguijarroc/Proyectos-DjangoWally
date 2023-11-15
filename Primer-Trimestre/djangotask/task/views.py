from django.shortcuts import render,redirect,get_object_or_404
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

class Task_list(View):
    tasks=Task.objects.all()
    template_name='task/tasks_list.html'
    def get(self, request):
        return render(request,self.template_name, {'tasks':self.actualizaTask()})
    def actualizaTask(self):
        self.tasks=Task.objects.all()
        return self.tasks
class Task_num(View):
    template_name='task/task_num.html'
    def get(self,request,pk):
        task=get_object_or_404(Task, pk=pk)
        '''
        form=TaskForm(instance=task)
        '''
        return render(request,self.template_name,{'task':task})
    def post(self):
        return self.get
    
        
class Task_form(View):
    template_name='task/task_form.html'
    def get(self, request):
        form=TaskForm()
        return render(request,self.template_name, {'form': form})
    def post(self,request):
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request,self.template_name,{'form': form})
class Task_edit(View):
    template_name='task/task_edit.html'
    def get(self,request,pk):
        task=get_object_or_404(Task,pk=pk)
        form=TaskForm(instance=task)
        return render(request,self.template_name,{'form': form,'task':task})
    def post(self,request,pk):
        task=get_object_or_404(Task,pk=pk)
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_num', pk=task.pk)
        return render(request,self.template_name,{'form': form,'task':task})
class Task_delete(View):
    def eliminarTarea(self,pk):
        task=get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('task_num')