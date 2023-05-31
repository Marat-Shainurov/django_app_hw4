from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('heading', 'slug', 'content', 'img', 'created', 'is_published', 'views')
