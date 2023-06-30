from main.models import Product, Version


def get_products_active(queryset):
    return queryset.filter(is_active=True)


def get_versions_by_prod(prod):
    return Version.objects.filter(product=prod)