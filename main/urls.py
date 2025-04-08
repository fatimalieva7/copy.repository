
from django.contrib import admin
from django.urls import path

from main import views
app_name = 'name'

urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]

