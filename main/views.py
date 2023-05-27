import os.path

from django.shortcuts import render

from main.models import Product


def index(request):
    all_products = Product.objects.all()

    context = {
        'products': all_products,
        'page_title': 'Main page'
    }
    return render(request, 'main/index.html', context)


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        img = request.POST.get('img')
        if not img:
            new_product = Product(name=name, description=description, price=price, stock=stock, img='media/device.jpeg')
            new_product.save()
        else:
            new_product = Product(name=name, description=description, price=price, stock=stock,
                                  img=os.path.join('media', img))
            new_product.save()
    context = {'page_title': 'Add a product'}
    return render(request, 'main/add_product.html', context)
