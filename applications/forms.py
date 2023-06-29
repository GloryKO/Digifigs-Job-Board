from django import forms
from .models import Applicants, Role

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicants
        fields = '__all__'
        

        # widgets = {
        #     'role': forms.Select(attrs={'class': 'form-select'})
        # }
