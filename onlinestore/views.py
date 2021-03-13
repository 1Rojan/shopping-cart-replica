from django.shortcuts import render, HttpResponse, get_object_or_404
from . models import Product, Category


from .serializers import CategorySerializer, ProductSerializer
from rest_framework import generics



class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()





def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'onlinestore/index.html', context)


def cat_products(request, slug):
    category = get_object_or_404(Category, slug = slug)
    products = Product.objects.filter(categories = category)
    context = {
        'products': products
    }
    return render(request, 'onlinestore/cat_products.html', context)

def show_product(request, slug):
    product = get_object_or_404(Product, slug= slug)
    context = {
        'product':product
    }
    return render(request, 'onlinestore/show.html', context)