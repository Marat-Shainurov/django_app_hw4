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


class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ('heading', 'content', 'img', 'is_published')
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(generic.UpdateView):
    model = Blog
    fields = None
    success_url = reverse_lazy('blog:blog_list')


class BlogDeleteView(generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')


def switch_publish_status(request, pk):
    blog_object = get_object_or_404(Blog, pk=pk)

    if blog_object.is_published:
        blog_object.is_published = False
    else:
        blog_object.is_published = True

    blog_object.save()

    slug = blog_object.slug
    return redirect(reverse('blog:blog_detail', kwargs={'slug': slug}))
