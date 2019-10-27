from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class feedback_new(models.Model):
    """
    Adding single Feedback
    """
    Title = models.CharField(max_length=200)
    feedback  = models.CharField(max_length=800)
    created_date = models.DateTimeField(auto_now_add=True)
    Score = models.IntegerField(default=0,validators=[MinValueValidator(1), MaxValueValidator(10)])
   
    def __str__(self):
        return self.Title