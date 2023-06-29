from django.urls import path

from . import views

urlpatterns = [
    path('applicants_list', views.ApplicantListView.as_view(), name='applicant_list'),
    #path('admin/applicant/<int:pk>/', views.AdminApplicantDetailView.as_view(), name='admin_applicant_detail'),
    path('', views.create_application, name='create_application'),
    path('applications/success',views.application_success,name='application_success'),
    path('applications/error',views.application_error,name='application_error')
]
