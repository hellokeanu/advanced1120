from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,name='index'),  # 1907
    path('createTodo/',views.createTodo,name='createTodo')
]
