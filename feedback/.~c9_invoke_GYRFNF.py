from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Feedback(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product_title = models.CharField(max_length=100)
    feedback = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    RATING_CHOICES = ((1, 'Poor'), (2, 'Average'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
