from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='prod_id')
    name = models.CharField(max_length=100, verbose_name='prod_name')
    description = models.TextField(verbose_name='prod_descr', **NULLABLE)
    price = models.IntegerField(verbose_name='prod_price')
    stock = models.IntegerField(verbose_name='prod_stock')
    img = models.ImageField(upload_to='media/', verbose_name='product_img', default='media/device.jpeg', **NULLABLE)

    def __str__(self):
        return f'{self.id} {self.name}'

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
