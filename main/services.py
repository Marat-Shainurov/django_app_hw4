from django.conf import settings
from django.core.cache import cache

from main.models import Version, Product, Category


def cache_products():
    if settings.CACHE_ENABLED:
        key = 'products_list'
        products_list = cache.get(key)
        if products_list is None:
            products_list = Product.objects.filter()
            cache.set(key, products_list)
        return products_list
    else:
        products_list = Product.objects.all()

    return products_list


def get_products_active(queryset):
    return queryset.filter(is_active=True)


def get_versions_by_prod(prod):
    return Version.objects.filter(product=prod)


def get_products_all(activity=True):
    return Product.objects.all(is_active=activity)


def get_categories_all_active(activity=True):
    return Category.objects.all(is_active=activity)


def get_categories_all_active_cache():

    if settings.CACHE_ENABLED:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.filter(is_active=True)
            cache.set(key, category_list)
        return category_list
    else:
        category_list = Category.objects.all(is_active=True)

    return category_list
