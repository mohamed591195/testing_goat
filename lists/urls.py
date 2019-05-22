from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('lists/<int:list_id>/add_item', views.AddItem, name='add-item'),
    path('lists/<int:list_id>/', views.ViewList, name='view-list'),
    path('lists/new', views.NewList, name='new-list'),
    
    
]
