from django.urls import path
from .views import register, profile, login_w, logout_w

urlpatterns = [
    path("profile/", profile, name="profile"),
    path("login/", login_w, name="login"),
    path("logout/", logout_w, name="logout"),
    path("register/", register, name="register"),
]