from django.shortcuts import render
from django.urls import reverse
from .forms import ApplicantForm
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView

from .models import Applicants

def create_application(request):
    if request.method == 'POST':
        application_form = ApplicantForm(request.POST)
        if application_form.is_valid():
            application_form.save()
            return HttpResponseRedirect(reverse('application_success'))
        else:
            return HttpResponseRedirect(reverse('application_error'))
    else:
        application_form = ApplicantForm()
        return render(request,'applications/create_application.html',{'application_form':application_form})
    

def application_success(request):
    return render(request,'applications/application_success.html') 

def application_error(request):
    return render(request,'applications/application_error.html')
    
    
 