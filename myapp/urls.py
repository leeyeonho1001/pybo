from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create), # type: ignore
    path('read/<id>/', views.read),
    path('delete/', views.delete) # type: ignore
]

