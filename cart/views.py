from django.shortcuts import render, redirect
from .cart import Cart
from store.models import Product

def add_product(request, product_id):
    
    cart = Cart(request)

    product = Product.objects.get(id=product_id)

    cart.add(product=product)

    return redirect("Store")

def remove_product(request, product_id):
    
    cart = Cart(request)

    product = Product.objects.get(id=product_id)

    cart.remove(product=product)

    return redirect("Store")

def subtract_product(request, product_id):
    
    cart = Cart(request)

    product = Product.objects.get(id=product_id)

    cart.subtract(product=product)

    return redirect("Store")

def clean_cart(request, product_id):
    
    cart = Cart(request)

    cart.clean()

    return redirect("Store")