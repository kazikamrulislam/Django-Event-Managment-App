from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('add_event/', views.add_event, name='add_event'),
]