from django.urls import path
from .views import fetch_top_products, fetch_product_details

urlpatterns = [
    path('categories/<str:category_name>/products', fetch_top_products, name='fetch-top-products'),
    path('categories/<str:category_name>/products/<str:product_id>', fetch_product_details, name='fetch-product-detail'),
]
