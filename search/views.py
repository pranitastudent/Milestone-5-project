from django.shortcuts import render
from products.models import Product

# Create your views here.

# Code adapted from Code Institute Ecoomerce App website

def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})