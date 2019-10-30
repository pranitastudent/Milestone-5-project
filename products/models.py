from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    SIZE_CHOICES = (
        ('small', 'SMALL'),
        ('medium', 'MEDIUM'),
        ('large', 'LARGE'),
        ('xl-large', 'XL-LARGE'),
        ('xx-large', 'XXL-LARGE'),
    )    
    size = models.CharField(max_length=6, choices=SIZE_CHOICES, default='small')
    COLOUR_CHOICES = (
        ('green', 'GREEN'),
        ('medium', 'YELLOW'),
        ('large', 'BLUE'),
    )    
    colour = models.CharField(max_length=6, choices=COLOUR_CHOICES, default='blue')   

    def __str__(self):
        return self.name