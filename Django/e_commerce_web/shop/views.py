from django.shortcuts import render , get_object_or_404
from .models import Product 
import random

# Create your views here.

def Shop(request):
    product = list(Product.objects.all())
    random.shuffle(product)
    return render ( request, 'shop/shop.html' ,{'Products' : product})

def Checkout(request):
    return render ( request,'shop/checkout.html')

def Product_Details(request, slug):
    product = Product.objects.get(slug = slug)
    return render (request, 'shop/single-product-details.html',{'product' : product})
