from django.shortcuts import render
from django.views import generic

from blog.models import Blog


class BlogListView(generic.ListView):
    model = Blog
