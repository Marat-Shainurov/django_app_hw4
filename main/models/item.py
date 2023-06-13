from django.db import models

from main.models import Product

NULLABLE = {'null': True, 'blank': True}


class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product_name')
    name = models.CharField(max_length=100, verbose_name='item_name')
    description = models.TextField(verbose_name='item_descr', **NULLABLE)
    price = models.IntegerField(verbose_name='item_price')
    stock = models.IntegerField(verbose_name='item_stock')
    img = models.ImageField(upload_to='media/items/', verbose_name='item_img')

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'
