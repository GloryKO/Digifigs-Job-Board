from django.db import models
# Create your models here.
from django import forms

ROLES_CHOICES =(
    
        ("FRONTEND DEVELOPER","FRONTEND DEVELOPER"),
        ("BACKEND DEVELOPER","BACKEND DEVELOPER"),
        ("PRODUCT DESIGNER","PRODUCT DESIGNER"),
        ("ML ENGINEER INTERN","ML ENGINEER INTERN"),
        ("DIGITAL MARKETING INTERN","DIGITAL MARKETING INTERN"),
        
        )

class Role(models.Model):
    available_roles = models.CharField(max_length=25,choices=ROLES_CHOICES)
    
    def __str__(self):
        return self.available_roles
    
    
class Applicants(models.Model):
    full_name = models.CharField(max_length=500)
    # last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    resume_link = models.URLField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
