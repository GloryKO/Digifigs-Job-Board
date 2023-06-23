from django.shortcuts import render
from .forms import ApplicantForm
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView

from .models import Applicant

#handle the admin list of applicants
class AdminApplicantListView(ListView):
    model = Applicant
    template_name = 'job_portal/admin_applicant_list.html'
    context_object_name = 'applicants'

#handle the detail of a single applicant 
class AdminApplicantDetailView(DetailView):
    model = Applicant
    template_name = 'job_portal/admin_applicant_detail.html'
    context_object_name = 'applicant'


def create_applicantion(request):
    if request.method == 'POST':
        application_form = ApplicantForm(request.POST)
        if application_form.is_valid():
            application_form.save()
            return render('job_portal:application_success')
    else:
        application_form = ApplicantForm()
        return render(request,'job_portal/create_application.html',{'application_form':application_form})
    
    
 