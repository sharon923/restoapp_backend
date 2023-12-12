from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.viewRest, name="view"),
    path('add/', views.addRest, name='add'),
    path('search/', views.searchRest, name='search'),
]
