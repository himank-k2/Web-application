from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
    path('insert/', views.insert),
    path('select/', views.select),
    path('update/<int:id>/', views.update),
    path('delete/<int:id>/', views.delete),
]

