from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, switch_publish_status, BlogCreateView

app_name = BlogConfig.name

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<str:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/switch/<int:pk>/', switch_publish_status, name='switch_publish_status'),
]
