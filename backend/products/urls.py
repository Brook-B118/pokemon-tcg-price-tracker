from django.urls import path
from . import views
# the "." means "current folder" so we only look for views from the current folder we are in.

# This app's URL Configuration, this needs to be imported into the root (main) url configuration as well.
urlpatterns = [
    path('', views.product_list, name='product_list'),  # Changed path for the product list
    path('<int:id>/<slug:name>/', views.product_detail, name='product_detail'),  # URL for product details
]