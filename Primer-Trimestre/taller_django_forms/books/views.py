from django.shortcuts import render,redirect,get_object_or_404
from .models import Book
from django.views import View
from .forms import BookForm

class List_book(View):
    books=Book.objects.all()
    template_name='books/book_list.html'
    def get(self, request):
        return render(request,self.template_name, {'books':self.actualizaBook()})
    def actualizaBook(self):
        self.books=Book.objects.all()
        return self.books
class Book_num(View):
    template_name='books/book_num.html'
    def get(self,request,pk):
        book=get_object_or_404(Book, pk=pk)
        render(request,self.template_name,{'book':book})
    def post(self):
        return self.get
    
        
class Form_book(View):
    template_name='books/book_form.html'
    def get(self, request):
        form=BookForm()
        return render(request,self.template_name, {'form': form})
    def post(self,request):
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request,self.template_name,{'form': form})
class Edit_book(View):
    template_name='books/book_edit.html'
    def get(self,request,pk):
        book=get_object_or_404(Book,pk=pk)
        form=BookForm(instance=book)
        return render(request,self.template_name,{'form': form,'book':book})
    def post(self,request,pk):
        book=get_object_or_404(Book,pk=pk)
        form=BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('book', pk=book.pk)
        return render(request,self.template_name,{'form': form,'book':book})
# Create your views here.
