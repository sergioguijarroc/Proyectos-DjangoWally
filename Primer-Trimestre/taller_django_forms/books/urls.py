from django.urls import path
from .views import List_book,Book_num,Form_book,Edit_book

urlpatterns = [
    path('', List_book.as_view(), name='list'),
    path('book/<int:pk>/',Book_num.as_view(),name='book'),
    path('book/new',Form_book.as_view(),name='form'),
    path('book/edit/<int:pk>/',Edit_book.as_view(),name='edit'),
]