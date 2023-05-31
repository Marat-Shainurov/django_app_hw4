from django.urls import reverse_lazy
from django.views import generic

from main.models import Product


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = 'Main page'
        return context


class ProductCreateView(generic.CreateView):
    model = Product
    fields = ('name', 'description', 'price', 'stock', 'img')
    success_url = reverse_lazy('main:product_list')
    extra_context = {
        'page_title': 'Add a product'
    }


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
