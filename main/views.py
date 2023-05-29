import os.path

from django.core.files.storage import default_storage
from django.core.paginator import Paginator
from django.shortcuts import render

from config import settings
from main.models import Product


def index(request):
    all_products = Product.objects.all()

    paginator = Paginator(all_products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'page_title': 'Main page'
    }
    return render(request, 'main/index.html', context)


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        img = request.FILES.get('img')

        new_product = Product(name=name, description=description, price=price, stock=stock, img=img)
        file_path = default_storage.save(f"media/{img}", img)
        new_product.img = file_path
        new_product.save()

    context = {'page_title': 'Add a product'}
    return render(request, 'main/add_product.html', context)


def promo_one(request):
    context = {'page_title': 'Promo one'}
    return render(request, 'main/promo_page_1.html', context)


def promo_two(request):
    context = {'page_title': 'Promo two'}
    return render(request, 'main/promo_page_2.html', context)
