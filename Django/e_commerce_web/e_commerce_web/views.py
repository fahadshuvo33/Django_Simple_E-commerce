from django.shortcuts import render , redirect
from shop.models import Product,Blog,Cart
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import random

def Home(request):
    product = list(Product.objects.all())
    random.shuffle(product)
    return render(request,'home.html' ,{'Products' : product})

def blog(request):
    blog = Blog.objects.all()
    return render(request,'blog.html' ,{'Blogs':blog})

def contactUs(request):
    return render ( request, 'contact.html')

def Blog_Details(request,slug):
    blog = Blog.objects.get(slug = slug)
    return render ( request, 'blog-details.html',{'blog' : blog})


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get_or_create(user=request.user)
    cart.products.add(product)
    cart.save()
    print(product,cart)
    # Add a success message to the user's session.
    messages.success(request, 'Product added to cart successfully!')

    # Render the current page again.
    return render(request, request.path)

def cart_detail(request):
    cart = Cart.objects.get(user=request.user)
    products = cart.products.all()[:3]

    context = {
        'Cart': cart,
        'Products': products,
    }

    return render(request, 'cart.html', context)



