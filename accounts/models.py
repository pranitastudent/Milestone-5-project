from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class Post(models.Model):
    """
    A single Blog post
    """
    title = models.CharField(max_length=200)
    feedback = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    Rating_CHOICES = (
    (1, 'Poor'),
    (2, 'Average'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent')
    )
    rating = models.IntegerField(choices=Rating_CHOICES, default=1)
    views = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title        