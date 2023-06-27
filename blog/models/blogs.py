from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from unidecode import unidecode

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    heading = models.CharField(max_length=250, verbose_name='heading', unique=True)
    slug = models.CharField(max_length=250, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='content')
    img = models.ImageField(upload_to='blog/', verbose_name='preview')
    created = models.DateTimeField(auto_now_add=True, verbose_name='creation date')
    is_published = models.BooleanField(default=True, verbose_name='is_published')
    views = models.IntegerField(verbose_name='views number', default=0, **NULLABLE)

    def __str__(self):
        return f'{self.heading} {self.slug}'

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.heading))
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.is_published = False
        self.save()

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        permissions = [
            (
                'set_published',
                'can publish/unpublish'
            )
        ]
