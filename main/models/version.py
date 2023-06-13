from django.db import models

from main.models import Product

NULLABLE = {'null': True, 'blank': True}


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product_name',
                                related_name='versions')
    name = models.CharField(max_length=100, verbose_name='version_name')
    description = models.TextField(verbose_name='version_descr', **NULLABLE)
    price = models.IntegerField(verbose_name='version_price')
    stock = models.IntegerField(verbose_name='version_stock')
    is_actual = models.BooleanField(verbose_name='is_actual_version')
    is_active = models.BooleanField(verbose_name='is_active', **NULLABLE, default=True)

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'version'
        verbose_name_plural = 'versions'
