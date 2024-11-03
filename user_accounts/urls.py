from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="account_home"),
    path("register/", views.registration, name="register"),
    path("login/", views.login_view, name="login"),
    path('logout/', views.user_logout, name='logout'),
]
