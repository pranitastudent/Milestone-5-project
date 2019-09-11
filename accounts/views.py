# Django Shortcuts

from django.shortcuts import render, redirect,get_object_or_404, reverse 
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from accounts.forms import UserLoginForm,  UserRegistrationForm
from .models import Feedback
from .forms import FeedbackPostForm

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

# Feedback Form

# Main Feedback Page

def feedback(request):
    """ Returns main feedback page"""
    return render(request,  'feedback.html')

# Save Feedback

def feedback_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    post = get_object_or_404(Feedback, pk=pk)
    post.views += 1
    post.save()
    return render(request, "feedbackdetail.html", {'post': post})

# Create or Edit Feedback

def create_or_edit_feedback(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    post = get_object_or_404(Feedback, pk=pk) if pk else None
    if request.method == "POST":
        form = FeedbackPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(feedback_detail, post.pk)
    else:
        form = FeedbackPostForm(instance=post)
    return render(request, 'feedbackform.html', {'form': form})