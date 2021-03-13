from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'onlinestore'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>', views.cat_products, name='cat_product'),
    path('product/<slug:slug>', views.show_product, name='show_product'),


    path('api/category', views.CategoryListView.as_view()),
    path('api/category/<int:pk>/', views.CategoryView.as_view()),

    path('api/product', views.ProductListView.as_view()),
    path('api/product/<int:pk>/', views.ProductView.as_view()),
]