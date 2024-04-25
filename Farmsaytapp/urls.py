from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('mission/', views.mission, name = 'mission'),
    path('plant/', views.plant, name = 'plant'),
    path('news/', views.news, name = 'news'),
    path('buy/', views.buy, name = 'buy'),
    path('catalog/', views.catalog, name = 'catalog'),
    path('news_card1/', views.news_card1, name = 'news_card1'),
    path('news_card2/', views.news_card2, name = 'news_card2'),
    path('news_card3/', views.news_card3, name = 'news_card3'),
    path('news_card4/', views.news_card4, name = 'news_card4'),
    path('urorens/', views.urorens, name = 'urorens'),
]