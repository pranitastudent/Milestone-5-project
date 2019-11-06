from django import forms

from .models import Feedback

class FeedbackForm(forms.ModelForm):
    """
    Create a Form so that the user can give feedback
    """
    class Meta:
        model = Feedback
        fields = ('product_title', 'user_feedback', 'rating' )