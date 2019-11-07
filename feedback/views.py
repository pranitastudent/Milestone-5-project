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
    
    return render(request, "feedback.html", {'posts': posts})


# Create Post - Only logged in users

@login_required()


#  Tutor Tim Nelson added with changes to Lines 44-46

def add_post(request):
    """
    This View allows logged in users
    to post there feedback about the product
    """
    
    if request.method=="POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=form.pk)
    else:
        form=FeedbackForm()
    return render(request, "feedbackform.html", {"form":form})
    

#  Post Detail- single view

@login_required()

def post_detail(request, pk):
    """
    This view allows logged in users
    to see there own feedback post about
    the product
    """
    post = get_object_or_404(Feedback, pk=pk)
    post.save()
    return render(request, "feedbackdetail.html", {"post":post})
    

    
#  Edit Post - Only Logged in Users and only there own

@login_required()

def edit_post(request,pk):
    """
    A view that allows user that created the post
    to edit there own
    """
    post=get_object_or_404(Feedback, pk=pk)
    if request.user == post.author:
        if request.method == "POST":
            form = FeedbackForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect(get_posts)
        else:
            form = FeedbackForm(instance=post)
        return render(request,"feedbackform.html", {"form":form})   
    else:
        messages.info(request, "You don't have permission to edit this feedback")
        form = FeedbackForm()
    return('add_post')  
    
    
# Delete Post - Only Logged in Users and only there own

@login_required()

def delete_post(request,pk):
    """
    A view that allows users which created the post to delete there
    own post
    """
    post=get_object_or_404(Feedback, pk=pk)
    if request.user == post.author:
        post.delete()
        messages.success(request, "Your Feedback Post has been deleted")
    else:
        messages.info(request, "You don't have permission to delete this feedback")
    return ('get_posts')    
 