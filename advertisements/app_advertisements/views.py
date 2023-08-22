from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Advertisements
from .forms import AdForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

def index(request):
    advertisement = Advertisements.objects.all()
    context = {'advertisements': advertisement}
    return render(request, 'app_advertisements/index.html', context)

def top_sellers(request):
    return render(request, 'app_advertisements/top-sellers.html')

@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.method == "POST":
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisements(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse("main-page")
            return redirect(url)
    else:
        form = AdForm()
    context = {"form": form}
    return render(request, 'app_advertisements/advertisement-post.html', context)

def register(request):
    return render(request, 'register.html')

def profile(request):
    return render(request, 'profile.html')

def login(request):
    return render(request, 'login.html')

def advertisement(request):
    return render(request, 'app_advertisements/advertisement.html')
