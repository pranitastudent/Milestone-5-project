# Django Shortcuts

from django.shortcuts import render, redirect,get_object_or_404, reverse, render_to_response 
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from accounts.forms import UserLoginForm,  UserRegistrationForm, ContactForm
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .models import feedback_new
import datetime
from .forms import FeedbackForm



# Index View

def index(request):
    """Return the index.html file"""
    return render(request,  'index.html')


# Logout View

def logout(request):
    """Log out the user"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!", 
                     extra_tags="alert-primary")
    return redirect(reverse('index'))

# Login View

def login(request):
    """Logs the user in"""
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in!", 
                         extra_tags="alert-primary")
        return redirect(reverse('index'))
        
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
            password = request.POST['password'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!", 
                                 extra_tags="alert-primary")
                if request.GET.get('next', False):
                    return HttpResponseRedirect(request.GET.get('next'))
                else:
                    return redirect(reverse('index'))
            else:
                login_form.add_error(None,
                "Your username or password is incorrect!")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})
    

# Registration View

def register(request):
    """Lets users register to site"""
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in", 
                         extra_tags="alert-primary")
        return redirect(reverse('index'))
        
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'],
            password=request.POST['password1'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered!", 
                                 extra_tags="alert-primary")
                return redirect(reverse('index'))
            else:
                messages.error(request, 
                               "Unable to register your account at this time!",
                               extra_tags="alert-danger")

    else:
        registration_form = UserRegistrationForm()
    return render(request, 'register.html', {
                  'registration_form': registration_form})

# Contact Form- Code adapted from (Django-2.2 Part-7 Django Contact Form with SMTP Email Backed Tutorial | By Creative web) 

def Contact(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST) 
        
        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            contact_content = request.POST.get('content')

            template = get_template('contact_form.txt')
            context = {
                'contact_name' : contact_name,
                'contact_email' : contact_email,
                'contact_content' : contact_content,
            }
            
            content = template.render(context)
        
        email = EmailMessage(
            "New contact form email",
            content,
            "Pranita's T-shirt Shop" + '',
            ['pranitacoder12@gmail.com'],
            headers = { 'Reply To': contact_email }
            
        )
            
        email.send()
            
        return render_to_response('success.html')
    return render(request, 'contact.html', {'form':Contact_Form })   
    
# Feedback


def Feedback(request):
    """
    Create a list of all feedback that was published
    until now abd render to template called feedback.html
    """
    
    posts = feedback_new.objects.all()
    return render(request, 'feedback.html',{'post': posts})
    
def Feedback_detail(request, pk):
    """
    
    Create a view that returns a single feedback published only by
    the user based on post ID render to feedback.html or return 404.
    """
    
    post = get_object_or_404(feedback_new)
    post.views += 1
    return render(request, 'feedbackdetail.html',{'post': post})
    
    
    
    
def create_or_edit_post(request, pk=None):
    """
    The user which created the post can edit or delete it.
    """
    post = get_object_or_404(feedback_new, pk=pk)
    
    
    