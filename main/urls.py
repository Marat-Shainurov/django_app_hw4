from django.urls import path

from main.apps import MainConfig
from main.views import index, add_product, promo_two

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_product, name='add'),
    path('promo_two/', promo_two, name='promo_two'),
    path('promo_one/', promo_two, name='promo_one')
]
