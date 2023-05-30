from django.urls import path

from main.apps import MainConfig
from main.views import PromoOneView, PromoTwoView, ProductListView, ProductCreateView

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('add/', ProductCreateView.as_view(), name='add'),
    path('promo_one/', PromoOneView.as_view(), name='promo_one'),
    path('promo_two/', PromoTwoView.as_view(), name='promo_two')
]
