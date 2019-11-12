from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError




class UserLoginForm(forms.Form):
    """Form for login page"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class UserRegistrationForm(UserCreationForm):
    """Form to allow users to register"""
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise ValidationError('Please confirm your password')
            
        if password1 != password2:
            raise ValidationError("Passwords must match!")
            
        return password2
        
# Contact Form- Code adapted from (Django-2.2 Part-7 Django Contact Form with SMTP Email Backed Tutorial | By Creative web) 

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.Textarea(attrs={
        "placeholder":" Please enter your name",
    }))
    contact_email = forms.EmailField(required=True, widget=forms.Textarea(attrs={
        "placeholder":"Please enter your email address",
    }))
    message = forms.CharField(required = True, widget=forms.Textarea(attrs={
        "rows":5,
        "placeholder":"Please enter your message",
    }))
    
