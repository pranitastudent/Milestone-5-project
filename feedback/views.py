from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Feedback
from django.shortcuts import render, get_object_or_404, redirect
from .forms import FeedbackForm



# Create your views here.

# Feedback Views- Adapted from Code Institute Blog Post lectures

# See All Feedback- All Visitors

def get_posts(request):
    """
    This View shows all feedback
    for all visitors to site
    """
    posts = Feedback.objects.filter(published_date__lte=timezone.now()
    ).order_by('-published_date')


# Create Post - Only logged in users

@login_required()

def add_post(request):
    """
    This View allows logged in users
    to post there feedback about the product
    """
    
    if request.method=="POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.author
            post.save()
            return redirect('get_posts', pk=post.pk)
    else:
        form=FeedbackForm()
    return render(request, "feedbackform.html", {"form":form})
    
    
#  Edit Post - Only Logged in Users and only there own

def edit_post(request,pk):
    """
    A view that allows user that created the post
    to edit there own
    """
    post=get_object_or_404(Feedback, pk=pk)
    if request.user == post.user:
        if request.method == "POST":
            form = FeedbackForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('get_posts', pk=post.pk)
        else:
            form = FeedbackForm(instance=post)
        return render(request,"feedabckform.html", {"form":form})   
    else:
        messages.info(request, "You don't have permission to edit this feedback")
        form = FeedbackForm()
    return('add_post')  
    
    
# Delete Post - Only Logged in Users and only there own

def delete_post(request,pk):
    """
    A view that allows users which created the post to delete there
    own post
    """
    post=get_object_or_404(Feedback, pk=pk)
    if request.user == post.user:
        post.delete()
        messages.success(request, "Your Feedback Post has been deleted")
    else:
        messages.info(request, "You don't have permission to delete this feedback")
    return ('get_posts')    
 