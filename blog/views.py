from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Blog


class BlogListView(generic.ListView):
    model = Blog


class BlogDetailView(generic.DetailView):
    model = Blog

# class BlogCreateView(generic.CreateView):
#     model = Blog
#     fields = None
#     success_url = reverse_lazy('blog:blog_detail')

#
# class BlogUpdateView(generic.UpdateView):
#     model = Blog
#     fields = None
#     success_url = reverse_lazy('blog:blog_detail')
#
#
# class BlogDeleteView(generic.DetailView):
#     model = Blog
#     success_url = reverse_lazy('blog:blog_list')
