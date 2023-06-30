from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm,CustomUserAuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_superuser = True
            user.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = CustomUserCreationForm()
    return render(request,'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect('dashboard')
    else:
        form = CustomUserAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

