from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('add_event/', views.add_event, name='add_event'),
    # path('event/<int:pk>/edit/', views.event_update, name='event_update'),
    # path('event/<int:pk>/delete/', views.event_delete, name='event_delete'),
]