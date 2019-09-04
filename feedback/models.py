from django.db import models
from django.utils import timezone

class Feedback(models.Model):
    """
    Allow User to import feedback 
    once purchased product
    """
    
    product_title = models.CharField(max_length=200)
    feedback = models.TextField()
    rating_product = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date =models.DateTimeField(blank=False, null=False, default=timezone.now)
    
    def __unicode__(self):
        return self.product_title