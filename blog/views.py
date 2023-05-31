from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Blog


class BlogListView(generic.ListView):
    model = Blog
    extra_context = {'page_title': 'Blogs'}


class BlogDetailView(generic.DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['page_title'] = 'Blog details'
        return context_data

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
