from django.urls import reverse_lazy
from django.views import generic

from main.models import Product


class ProductListView(generic.ListView):
    model = Product
    template_name = 'main/product_list.html'
    context_object_name = 'object_list'
    paginate_by = 3
    page_title = 'Main page'


class ProductCreateView(generic.CreateView):
    model = Product
    fields = ('name', 'description', 'price', 'stock', 'img')
    success_url = reverse_lazy('main:product_list')


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
