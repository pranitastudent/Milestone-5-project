from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Feedback(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    product_title = models.CharField(max_length=100)
    feedback = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    Rating_CHOICES = (
    ('Poor', 'Poor'),
    ('Average', 'Average'),
    ('Good', 'Good'),
    ('Very Good', 'Very Good'),
    ('Excellent', 'Excellent')
    )
    rating = models.IntegerField(choices=Rating_CHOICES, default=None)
    views = models.IntegerField(default=0)
    