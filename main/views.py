from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import generic

from main.forms import ProductForm, VersionForm
from main.models import Product, Version


class ProductListView(LoginRequiredMixin, generic.ListView):
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
        return reverse('main:product_detail', args=[self.kwargs.get('slug')])

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

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)

        if self.object.user_product != self.request.user and not self.request.user.is_staff:
            raise Http404('This is not your product! You can only edit product that have been added by you.')

        content_type = ContentType.objects.get_for_model(Product)
        permissions = Permission.objects.get(
            codename="change_product",
            content_type=content_type
        )
        self.request.user.user_permissions.add(permissions)
        return self.object



class ProductDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Product
    success_url = reverse_lazy('main:product_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)

        if self.object.user_product != self.request.user and not self.request.user.is_staff:
            raise Http404('This is not your product! You can only delete product that have been added by you.')

        content_type = ContentType.objects.get_for_model(Product)
        permissions = Permission.objects.get(
            codename="delete_product",
            content_type=content_type
        )
        self.request.user.user_permissions.add(permissions)
        return self.object


def make_unpublished(request, slug):
    if not request.user.is_staff:
        raise Http404('The publish/unpublish button is only available for moderators.')
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
