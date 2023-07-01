
from django.db import models
from django.utils.text import slugify
from unidecode import unidecode

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    category_name = models.CharField(max_length=250, verbose_name='category_name', unique=True)
    slug = models.SlugField(verbose_name='slug', **NULLABLE)
    category_description = models.TextField(verbose_name='category_description', **NULLABLE)
    is_active = models.BooleanField(verbose_name='is_active', default=True)

    def __str__(self):
        return f'{self.category_name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.category_name))
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
