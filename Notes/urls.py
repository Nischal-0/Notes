from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('create',views.create,name='create')
    # path('edit/<id>', views.edit),
    # path('delete/<id>', views.delete),
]
    
