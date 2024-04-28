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

def news_card1(request):
    return render(request, "news_card1.html")

def news_card2(request):
    return render(request, "news_card2.html")

def news_card3(request):
    return render(request, "news_card3.html")

def news_card4(request):
    return render(request, "news_card4.html")

def urorens(request):
    return render(request, "urorens.html")