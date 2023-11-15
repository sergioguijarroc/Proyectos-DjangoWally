from django.urls import path
from .views import Task_list, Task_num, Task_form, Task_edit, Task_delete

urlpatterns = [
    path("task/", Task_list.as_view(), name="task_list"),
    path("task/<int:pk>/", Task_num.as_view(), name="task_num"),
    path("task/new", Task_form.as_view(), name="task_form"),
    path("task/edit/<int:pk>/", Task_edit.as_view(), name="task_edit"),
    path("task/", Task_delete.as_view(), name="task_delete"),
]
