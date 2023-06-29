from main.models import Product


def get_products_active(queryset):
    return queryset.filter(is_active=True)
