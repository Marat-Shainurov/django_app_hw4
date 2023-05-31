from django.core.exceptions import ValidationError
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    heading = models.CharField(max_length=250, verbose_name='heading', unique=True)
    slug = models.CharField(max_length=250, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='content')
    img = models.ImageField(upload_to='blog/', verbose_name='preview')
    created = models.DateTimeField(auto_now_add=True, verbose_name='creation date')
    is_published = models.BooleanField(default=True, verbose_name='is_published')
    views = models.IntegerField(verbose_name='views number', default=0)

    def __str__(self):
        return f'{self.heading} {self.slug}'

    def save(self, *args, **kwargs):
        slug = ''
        for char in self.heading:
            if char.isalnum() or char == ' ':
                slug += char
        self.slug = slug.replace(' ', '-')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
