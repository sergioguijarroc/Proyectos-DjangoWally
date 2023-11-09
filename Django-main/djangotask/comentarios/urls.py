from django.urls import path
from . import views

urlpatterns = [
    path('comentarios/', views.formulario, name='formulario'),
    path('comentarios/confirmacion',views.confirmacion,name='confirmacion'),
    path('comentarios/lista_comentarios',views.lista_comentarios,name='lista_comentarios'),

]