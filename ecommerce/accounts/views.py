# Importing of django shortcuts

from django.shortcuts import render, redirect, reverse 
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required 
from accounts.forms import UserLoginForm,  UserRegistrationForm

# Index View

def index(request):
    """Return the index.html file"""
    return render(request,  'index.html')


# Logout View
    
@login_required
def logout(request):
    """Logs the user out - logout.html"""
    auth.logout(request)
    messages.success(request, "You have succesfully logged out , if you wish to pruchase products please login in!")
    return redirect(reverse('index'))

# Login View
    
def login(request):
    """Logs user in - pruchase item(s) in cart"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!") 
                return redirect (reverse('index'))
            else: 
                login_form.add_error(None, "Your username or password is incorrect!")
    else:
        login_form = UserLoginForm() 
    return render(request, 'login.html', {"login_form": login_form})

# Registration View
    
def registration(request):
    """ User Registration"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
        
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
           registration_form.save()
           
           user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            
           if user:
               auth.login(user=user, request=request)
               messages.success(request, "You have succesfully registered!")
               return redirect(reverse('index'))
           else:
               messages.error(request, "Unable to register your account at this time!")
                                       
            
    else:        
        registration_form=UserRegistrationForm()
        
    return render(request, 'registration.html', {
        "registration_form":registration_form})