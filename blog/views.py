from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
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

        self.object.views += 1
        self.object.save()

        return context_data


def switch_publish_status(request, slug):
    blog_object = get_object_or_404(Blog, slug=slug)

    if blog_object.is_publushed:
        blog_object.is_published = False
    else:
        blog_object.is_published = True

    return redirect(reverse('main: blog_detail'))

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
