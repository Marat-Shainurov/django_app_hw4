from django.shortcuts import render

from main.models import Product


def index(request):
    all_products = Product.objects.all()

    context = {
       'products': all_products
    }
    return render(request, 'main/index.html', context)
