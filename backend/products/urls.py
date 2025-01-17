from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # URL for listing all products
    path('<int:id>/', views.product_detail, name='product_detail'),  # URL for product details
]