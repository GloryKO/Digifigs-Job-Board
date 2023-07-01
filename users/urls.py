from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login_view,name='login'),
    path('dashboard',views.ApplicantsListView.as_view(),name='dashboard'),
    path('dashboard/<int:pk>/',views.ApplicantDetailView.as_view(),name='dashboard_detail')
]