from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name='main'),
    path('again/', views.again, name='again'),
    path('write/', views.write, name='write'),
]
