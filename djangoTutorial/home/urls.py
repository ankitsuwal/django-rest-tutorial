from django.urls import path
from .views import Home, ToDo

urlpatterns = [
    path(r'', Home.as_view()),
    path(r'todo/', ToDo.as_view(), name='todo'),
]
