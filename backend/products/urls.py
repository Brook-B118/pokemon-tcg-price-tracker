from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page at the root of the site 
    path('products/', views.product_list, name='product_list'),  # Changed path for the product list
    path('<int:id>/<slug:name>/', views.product_detail, name='product_detail'),  # URL for product details
]