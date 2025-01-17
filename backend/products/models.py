from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)  # Product name
    slug = models.SlugField(unique=True)  # Slug to use in the URL (for SEO-friendly URLs)
    description = models.TextField()  # Product description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product
    image = models.ImageField(upload_to='product_images/')  # Path to product image
    created_at = models.DateTimeField(auto_now_add=True)  # Date the product was created

    def __str__(self):
        return self.name