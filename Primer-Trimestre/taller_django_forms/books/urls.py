from django.urls import path
from .views import List_book,Book_num,Create_book,Update_book,Delete_book

urlpatterns = [
    path('', List_book.as_view(), name='list'),
    path('book/<int:pk>/',Book_num.as_view(),name='book'),
    path('book/new',Create_book.as_view(),name='form'),
    path('book/edit/<int:pk>/',Update_book.as_view(),name='update'),
    path('book/delete/<int:pk>/',Delete_book.as_view(),name='delete'),
]