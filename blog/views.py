from django.shortcuts import render
from blog.models import Category, Post

def blog(request):

    posts = Post.objects.all()

    ctx = {'posts' : posts}

    return render(request, "blog/blog.html", ctx)

def category(request, category_id):

    category = Category.objects.get(id=category_id)

    posts = Post.objects.filter(categories= category)

    return render(request, "blog/categories.html", {"category" : category, 'posts' : posts})