from django.contrib import admin

from main.models import Product
from main.models.version import Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'img', 'is_active')


@admin.register(Version)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock', 'img')
