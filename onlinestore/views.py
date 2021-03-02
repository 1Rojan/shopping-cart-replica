from django.shortcuts import render, HttpResponse, get_object_or_404
from . models import Product, Category

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