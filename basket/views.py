from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from onlinestore.models import Product, Category
from basket.basket import Basket


def add_basket(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)
        basketqty = basket.__len__()

        response = JsonResponse({'qty': basketqty})
        return response
