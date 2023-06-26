from django.conf import settings
from django.db import models
from django.utils.text import slugify
from unidecode import unidecode

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='prod_name', unique=True)
    slug = models.SlugField(verbose_name='slug', **NULLABLE)
    description = models.TextField(verbose_name='prod_descr', **NULLABLE)
    img = models.ImageField(upload_to='media/', verbose_name='product_img')
    is_active = models.BooleanField(verbose_name='is_active', **NULLABLE, default=True)
    user_product = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                                     verbose_name='user')
    is_published = models.BooleanField(verbose_name='is_published', default=False, **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        permissions = [
            ('set_published',
             'can publish/make unpublished'
             )
        ]
