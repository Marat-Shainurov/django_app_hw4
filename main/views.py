from django.urls import reverse_lazy, reverse
from django.views import generic

from main.forms import ProductForm
from main.models import Product


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = 'Main page'
        return context

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_active=True)
        return queryset


class ProductDetailView(generic.DetailView):
    model = Product


class ProductCreateView(generic.CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:product_list')
    extra_context = {
        'page_title': 'Add a product'
    }


class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('main:product_detail', args=[self.kwargs.get('slug')])


class ProductDeleteView(generic.DeleteView):
    model = Product
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
