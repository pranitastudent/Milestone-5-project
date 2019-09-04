from django import forms
from .models import Feedback

class Feedback_User_Form(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('product_title', 'feedback', 'rating_product')