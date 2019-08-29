from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

# Login Form

class UserLoginForm(forms.Form):
    """Form to login users """
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# Registration Form    
    
class UserRegistrationForm(UserCreationForm):
    """Form to register users"""
    
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput)
    
    class Meta:
        model= User
        fields = ['email', 'username', 'password1', 'password2']
    
# Form Validation

    def clean_email(self):
        email = self.cleaned_data.get('email')