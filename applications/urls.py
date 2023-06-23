from django.urls import path

from . import views

app_name = 'job_portal'

urlpatterns = [
    #path('', views.ApplicantListView.as_view(), name='applicant_list'),
    #path('applicant/<int:pk>/', views.ApplicantDetailView.as_view(), name='applicant_detail'),
    #path('admin/applicants/', views.AdminApplicantListView.as_view(), name='admin_applicant_list'),
    #path('admin/applicant/<int:pk>/', views.AdminApplicantDetailView.as_view(), name='admin_applicant_detail'),
    path('', views.create_applicantion, name='create_applicantion'),
]
