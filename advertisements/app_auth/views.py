from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'app_auth/register.html', {'form': form})

def profile(request):
    return render(request, 'app_auth/profile.html')

def login_w(request):
    redirect_url = reverse('profile')
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html', {"error": "Пользователь не найден"})

def logout_w(request):
    logout(request)
    return redirect(reverse('login'))