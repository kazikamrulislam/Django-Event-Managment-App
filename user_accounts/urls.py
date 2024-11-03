from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="account_home"),
    path("register/", views.registration, name="register"),
    path("login/", views.login_view, name="login"),
    path('profile/', views.user_profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
]
