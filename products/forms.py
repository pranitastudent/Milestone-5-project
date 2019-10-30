from .models import Product


class Product(forms.ModelForm):
    class Meta:
        model = Product
        fields['size']