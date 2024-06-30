from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from .models import AppUser
from .forms import RegisretForm

# Create your views here.
class AuthLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = '/'


class RegisterView(CreateView):
    model = AppUser
    form_class = RegisretForm
    template_name = 'users/register.html'
    success_url = '/'

class ProfileView(DetailView):
    model = AppUser
    template_name = 'users/profile.html'





