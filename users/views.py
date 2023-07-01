from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm,CustomUserAuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView,DetailView
from applications.models import Applicants

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

class ApplicantsListView(ListView):
    model = Applicants
    context_object_name ='applicants'
    template_name='users/applicants_list.html'
    
class ApplicantDetailView(DetailView):
    model= Applicants
    context_object_name='applicant_detail'
    template_name ='users/applicant_detial.html'
    