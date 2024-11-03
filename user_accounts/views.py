from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


class CustomeUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields =[
            "username",
            "email",
            "first_name",
            "last_name"
        ]

# AbstractUser
def registration(request):
    if request.method ==  "POST":
        form = CustomeUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("register")
    else:
        form = CustomeUserCreationForm()
        
    context = {
        "form": form,
    }
    return render(request, "accounts/register.html", context) 

def home(request):
    return render(request, "home.html")

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("account_home")
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, "accounts/login.html", context)

def user_logout(request):
    logout(request)
    return redirect("account_home")