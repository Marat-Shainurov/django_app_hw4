from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from blog.models import Blog
from blog.services import send_email_hundred_views


class BlogListView(generic.ListView):
    model = Blog
    extra_context = {'page_title': 'Blogs'}

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(generic.DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['page_title'] = 'Blog details'

        self.object.views += 1
        self.object.save()

        if self.object.views == 100:
            send_email_hundred_views()

        return context_data


class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ('heading', 'content', 'img', 'is_published')

    def get_success_url(self):
        return reverse_lazy('blog:blog_detail', kwargs={'slug': self.object.slug})


class BlogUpdateView(generic.UpdateView):
    model = Blog
    fields = ('heading', 'content', 'img', 'is_published')

    def get_success_url(self):
        return reverse_lazy('blog:blog_detail', kwargs={'slug': self.object.slug})


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
