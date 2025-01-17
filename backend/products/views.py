from django.shortcuts import render # Using Render to return dynamically loaded templates
from .models import Product

# Create your views here. These are request handlers.

# List all products
def product_list(request):
    products = Product.objects.all()  # Get all products from the database
    return render(request, 'products/product_list.html', {'products': products})

# View a specific product's details
def product_detail(request, id, slug):
    try:
        product = Product.objects.get(id=id, slug=slug)  # Fetch product by id and slug
        return render(request, 'products/product_detail.html', {'product': product})
    except Product.DoesNotExist:
        # Return a 404 error page if product not found
        return render(request, 'products/product_not_found.html')