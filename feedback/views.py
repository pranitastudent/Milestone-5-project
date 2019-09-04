from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Feedback
from .forms import Feedback_User_Form

def get_feedback(request):
    """
    Create a view that will return
    a list of the feedback which was
    published prior to now and render to feedback.html template
    """
    
    feedback = Feedback.objects.filter(published_date__lte=timezone.now
           ()).order_by('-published_date')
    return render(request, "feedback.html", {'feedback':feedback})       
    
    
def feedback_user(request, pk):
    """
    Create a view that reruns feedback from single user
    returns one set of feedback based on feedback id
    and render it to feedback_user.html template or return
    an error is feedback not found
    """
    feedback = get_object_or_404(Feedback, pk=pk)
    feedback.views += 1
    feedback.save()
    return render(request, "feedback_user.html", {'feedback':feedback})
    
def create_or_edit_feedback(request, pk=None):
    """
    User creates feedback and can only edit their own
    """
    feedback = get_object_or_404(Feedback, pk=pk)
    if request.method == "POST":
        form = Feedback_User_Form(request.POST, request.FILES, instance=feedback)
        if form.is_valid():
            post = form.save()
            return redirect(feedback_user, post.pk)
    else:
        form=Feedback_User_Form(instance=feedback)
    return render(request, 'feedbackuser.html', {'form':form})    