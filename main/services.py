from django.conf import settings
from django.core.cache import cache

from main.models import Version, Product


def cache_products():

    if settings.CACHE_ENABLED:
        key = 'products_list'
        products_list = cache.get(key)
        if products_list is None:
            products_list = Product.objects.all()
            cache.set(key, products_list)
        return products_list
    else:
        products_list = Product.objects.all()

    return products_list


def get_products_active(queryset):
    return queryset.filter(is_active=True)


def get_versions_by_prod(prod):
    return Version.objects.filter(product=prod)