from django.shortcuts import render




def index(request):
    return render(request, "index.html")

def mission(request):
    return render(request, "mission.html")

def plant(request):
    return render(request, "plant.html")

def news(request):
    return render(request, "news.html")

def buy(request):
    return render(request, "buy.html")

def catalog(request):
    return render(request, "catalog.html")