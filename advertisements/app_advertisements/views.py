from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisements

def index(request):
    advertisement = Advertisements.objects.all()
    context = {'advertisements': advertisement}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    return render(request, 'advertisement-post.html')

def register(request):
    return render(request, 'register.html')

def profile(request):
    return render(request, 'profile.html')

def login(request):
    return render(request, 'login.html')

def advertisement(request):
    return render(request, 'advertisement.html')