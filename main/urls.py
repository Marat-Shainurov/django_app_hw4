from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import PromoOneView, PromoTwoView, ProductListView, ProductCreateView, ProductDetailView, \
    ProductUpdateView, ProductDeleteView, make_unpublished

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='add'),
    path('product/<str:slug>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product/unpublish/<str:slug>/', make_unpublished, name='make_unpublished'),
    path('product/update/<str:slug>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<str:slug>/', ProductDeleteView.as_view(), name='product_delete'),
    path('promo_one/', cache_page(60)(PromoOneView.as_view()), name='promo_one'),
    path('promo_two/', cache_page(60)(PromoTwoView.as_view()), name='promo_two')
]
