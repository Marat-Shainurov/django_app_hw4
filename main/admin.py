from django.contrib import admin

from main.models import Product
from main.models.category import Category
from main.models.version import Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'user_product', 'img', 'is_active')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'price', 'stock', 'is_active')
    list_filter = ('product',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category_name', 'is_active', 'category_description')
    list_filter = ('category_name',)
