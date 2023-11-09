from django.urls import path
from . import views

urlpatterns = [
    path('comentarios/', views.comentarios, name='comentarios'),
    path('comentarios/',views.confirmacion,name='confirmacion')
]