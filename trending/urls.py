from django.urls import path
from trending.views import Trending_page,Trending_detail,trending_top1_detail,trending_top2_detail
from . import views
urlpatterns = [

path('trending/<slug:slug>/', Trending_detail.as_view(), name = 'trending_detail'),
path('trending_page/', views.Trending_page, name = 'trending_page'),
path('trending_top1_detail/<slug:slug>/', trending_top1_detail.as_view(), name = 'trending_top1_detail'),
path('trending_top2_detail/<slug:slug>/', trending_top2_detail.as_view(), name = 'trending_top2_detail'),

]

