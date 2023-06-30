from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields =('name','email',)

class CustomUserAuthenticationForm(AuthenticationForm):
    class Meta:
        model= CustomUser
        fields = ('email', 'password')
        