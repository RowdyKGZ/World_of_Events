from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm

from .models import *
from .form import *


def register_page(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form }
    return render(request, 'registration/register.html', context)

def login_page(request):
    context = {}
    return render(request, 'registration/login.html', context)