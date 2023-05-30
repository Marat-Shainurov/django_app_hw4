import os.path

from django.core.files.storage import default_storage
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from config import settings
from main.models import Product


class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'page_obj'
    paginate_by = 3
    page_title = 'Main page'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = self.page_title
        return context


#
# def index(request):
#     all_products = Product.objects.all()
#
#     paginator = Paginator(all_products, 3)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     context = {
#         'page_obj': page_obj,
#         'page_title': 'Main page'
#     }
#     return render(request, 'main/product_list.html', context)
#


class ProductCreateView(generic.CreateView):
    model = Product
    fields = ('name', 'description', 'price', 'stock', 'img')
    success_url = reverse_lazy('main:product_list')
#
#
# def add_product(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         price = request.POST.get('price')
#         stock = request.POST.get('stock')
#         img = request.FILES.get('img')
#
#         new_product = Product(name=name, description=description, price=price, stock=stock, img=img)
#         file_path = default_storage.save(f"media/{img}", img)
#         new_product.img = file_path
#         new_product.save()
#
#     context = {'page_title': 'Add a product'}
#     return render(request, 'main/product_form.html', context)


class PromoOneView(generic.TemplateView):
    template_name = 'main/promo_page_1.html'
    extra_context = {
        'page_title': 'Promo one'
    }


class PromoTwoView(generic.TemplateView):
    template_name = 'main/promo_page_2.html'
    extra_context = {
        'page_title': 'Promo two'
    }
