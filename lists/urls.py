from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('lists/the-only-list-in-the-world/', views.ViewList, name='view-list'),
    path('lists/new', views.NewList, name='new-list')
]
