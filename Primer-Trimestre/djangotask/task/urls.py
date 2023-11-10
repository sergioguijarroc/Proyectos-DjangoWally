from django.urls import path
from . import views
from .views import MyView

urlpatterns = [
    path('task/', MyView.as_view(), name='task'),
]
