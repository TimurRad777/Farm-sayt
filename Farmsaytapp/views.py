from django.shortcuts import render
from .models import Post, Product


def index(request):
    return render(request, "index.html")

def mission(request):
    return render(request, "mission.html")

def plant(request):
    return render(request, "plant.html")

def news(request):
    news = Post.objects.all()
    return render(request, "news.html", {'news':news})

def buy(request):
    return render(request, "buy.html")

def catalog(request):
    catalog = Product.objects.all()
    return render(request, "catalog.html", {'catalog': catalog})

def news_card(request, slug):
    news = Post.objects.get(slug__iexact = slug)
    return render(request, "news_card.html", {'news':news})

def product_detail(request, slug):
    product = Product.objects.get(slug__iexact = slug)
    return render(request, "product_detail.html", {'product': product})