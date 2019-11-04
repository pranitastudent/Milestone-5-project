from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    Size_CHOICES = (
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
    ('XLarge', 'XLarge'),
    ('XXLarge', 'XXLarge')
    )
    rating = models.IntegerField(choices=Size_CHOICES, default='Medium')

    def __str__(self):
        return self.name