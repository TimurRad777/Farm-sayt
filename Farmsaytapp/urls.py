from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('mission/', views.mission, name = 'mission'),
    path('plant/', views.plant, name = 'plant'),
    path('news/', views.news, name = 'news'),
    path('buy/', views.buy, name = 'buy'),
    path('catalog/', views.catalog, name = 'catalog'),
    path('news_card/<slug:slug>/', views.news_card, name = 'news_card'),
    path('product_detail/', views.product_detail, name = 'product_detail'),
]