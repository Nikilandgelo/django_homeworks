from django.urls import path
from phones.views import index, show_catalog, show_product

urlpatterns = [
    path('', index),
    path('catalog/', show_catalog, name='catalog'),
    path('catalog/<slug:slug>/', show_product),
]