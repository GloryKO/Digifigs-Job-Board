from django import forms
from .models import Applicants, Role

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicants
        fields = ('first_name', 'last_name', 'address', 'phone_number', 'resume_link', 'role')
        

        # widgets = {
        #     'role': forms.Select(attrs={'class': 'form-select'})
        # }
