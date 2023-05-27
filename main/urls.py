from django.urls import path

from main.views import index, add_product

urlpatterns = [
    path('', index),
    path('add/', add_product)
]
