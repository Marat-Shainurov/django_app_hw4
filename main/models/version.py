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
    is_active = models.BooleanField(verbose_name='is_active', **NULLABLE, default=True)

    def __str__(self):
        return f'{self.name} {self.price}'

    def save(self, *args, **kwargs):
        if self.is_active:
            for version in self.product.versions.all():
                if version.is_active and version is not self:
                    version.is_active = False
                    version.save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'version'
        verbose_name_plural = 'versions'
