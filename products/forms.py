from .models import Product


class Product(ModelForm):
    class Meta:
        model = Product
        fields['size']