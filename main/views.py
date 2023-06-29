from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import generic

from main.forms import ProductForm, VersionForm
from main.models import Product, Version
from main.services import get_products_active


class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product
    paginate_by = 3
    ordering = 'pk'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = 'Main page'
        return context

    def get_queryset(self, *args, **kwargs):
        if settings.CACHE_ENABLED:
            key = 'prod_list'
            prod_list = cache.get(key)
            print('Cached data is used')
            if prod_list is None:
                queryset = super().get_queryset(*args, **kwargs)
                prod_list = get_products_active(queryset)
                cache.set(key, prod_list)
            return prod_list
        else:
            queryset = super().get_queryset(*args, **kwargs)
            prod_list = get_products_active(queryset)
            print('DB data is used')
        return prod_list


class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:product_list')
    extra_context = {
        'page_title': 'Add a product'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        self.object.user_product = self.request.user
        self.object.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        else:
            print(formset.errors)
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        group = Group.objects.get(name="moderator")
        if not self.request.user.groups.filter(name=group).exists():
            permission = Permission.objects.get(codename="change_product")
            self.request.user.user_permissions.remove(permission)
            self.request.user.save()
        return reverse('main:product_detail', args=[self.kwargs.get('slug')])

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)

        if not self.request.user.has_perm('main.change_product') and self.request.user != self.object.user_product:
            raise Http404('You can\'t edit product that have not been added by you!')
        elif not self.request.user.has_perm('main.change_product') and self.request.user == self.object.user_product:
            content_type = ContentType.objects.get_for_model(Product)
            permissions = Permission.objects.get(
                codename="change_product",
                content_type=content_type
            )
            self.request.user.user_permissions.add(permissions)
        return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        else:
            print(formset.errors)
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Product
    success_url = reverse_lazy('main:product_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)

        if self.object.user_product != self.request.user:
            raise Http404('This is not your product! You can only delete product that have been added by you.')

        return self.object


@permission_required('main.set_published')
def make_unpublished(request, slug):
    if not request.user.has_perm('main.set_published'):
        raise Http404('set_published_product permission is needed!')
    product = Product.objects.get(slug=slug)
    product.is_published = not product.is_published
    product.save()
    return redirect(reverse('main:product_detail', kwargs={'slug': slug}))


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
