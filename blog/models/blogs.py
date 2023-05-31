from django.db import models


class Blog(models.Model):
    heading = models.CharField(max_length=100, verbose_name='heading')
    slug = models.CharField(max_length=100, verbose_name='slug')
    content = models.TextField(verbose_name='content')
    img = models.ImageField(upload_to='blog/', verbose_name='preview')
    created = models.DateTimeField(auto_now_add=True, verbose_name='creation date')
    is_published = models.BooleanField(default=True, verbose_name='is_published')
    views = models.IntegerField(verbose_name='views number')

    def __str__(self):
        return f'{self.heading} {self.slug}'

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
