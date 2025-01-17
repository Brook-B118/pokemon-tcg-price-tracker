from django.apps import AppConfig

# This file should really just be called config...

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
