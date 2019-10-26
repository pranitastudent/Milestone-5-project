from django.db import models
from django.utils import timezone


class feedback_new(models.Model):
    """
    Adding single Feedback
    """
    Title = models.CharField(max_length=200)
    feedback  = models.CharField(max_length=800)
   
    def __str__(self):
        return self.Title