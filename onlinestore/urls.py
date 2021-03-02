from django.urls import path
from . import views

app_name = 'onlinestore'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>', views.cat_products, name='cat_product'),
    path('product/<slug:slug>', views.show_product, name='show_product'),
]