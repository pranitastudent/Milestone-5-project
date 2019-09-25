from django.db import models
from django.utils import timezone


class Feedback(models.Model):
    """
    Adding single Feedback
    """
    product_title = models.CharField(max_length=200)
    feedback  = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
  
    def __str__(self):
        return 'feedback.html'