from django.shortcuts import render
from .models import Product

def store(request):

    products = Product.objects.all()

    ctx = {"products": products}

    return render(request, "store/store.html", ctx)