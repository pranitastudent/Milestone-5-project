# Django Shortcuts

from django.shortcuts import render, redirect,get_object_or_404, reverse, render_to_response 
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from .forms import UserLoginForm,  UserRegistrationForm, ContactForm, FeedbackForm
from django.core.mail import EmailMessage
from django.template.loader import get_template
import datetime
from .models import Post


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
    
# Feedback Form - The code below is adapated from the Code Institute Lectures on Blog Post

# View All Feedback - even if not own

def get_posts(request):
    """
    Create a view that will return a list
    of Posts that were published prior to 'now'
    and render them to the 'feedback.html' template
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "feedback.html", {'posts': posts})

# View Own Feedback and decide to post

@login_required
def post_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'feedbackdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_authenticated():
       user = request.user
       post.views += 1
       post.save()
    return render(request, "feedbackdetail.html", {'post': post})

# Add Creating and Editing/Deleting Feedback

@login_required
def create_or_edit_post(request, pk=None):
    """
    Create a view that allows us to create
    or edit a feedback post depending if the Post ID
    is null or not
    """
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
          form = FeedbackForm(request.POST, request.FILES, instance=post)
          if form.is_valid():
             post = form.save()
          return redirect(post_detail, post.pk)
    else:
        form = FeedbackForm(instance=post)
    return render(request, 'feedbackform.html', {'form': form})
    
    
# Delete Function


# Code for delete_post adapted from Try Django 1.9 - 23 of 38 - Delete View - website in references

@login_required
def delete_post(request, pk=None):
    
    """
    Create a view that allows the selected user to delete a post_detail
    """
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_authenticated():
        
       user = request.user
       post.user = request.user
       post.delete()

    return redirect("get_posts")
    

            
