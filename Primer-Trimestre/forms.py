from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import MyForm
class MyView(View):
    form=MyForm
    template_name="form.template.html"
    def get(self, request):
        self.form=MyForm(initial={"key":"value"})
        return render(request,self.template_name, {'form': self.form})
    def post(self,request):
        self.form=MyForm(request.POST)
        if self.form.is_valid():
            return HttpResponseRedirect('/thanks/')
        return render(request,self.template_name, {'form': self.form})