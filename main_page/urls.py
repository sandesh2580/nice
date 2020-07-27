from django.urls import path
from trending.views import Trending_page,Trending_detail
from . import views
from trending import views as trending_views
from main_page.views import homepage_body
urlpatterns = [

path ('', views.homepage, name = 'homepage'),
path('trending_top1/', trending_views.trending_top_1, name = 'trending_top1'),
path('trending_top2/', trending_views.trending_top_2, name = 'trending_top2'),
path('trending_top3/', trending_views.trending_top_3, name = 'trending_top3'),
path('trending_top4/', trending_views.trending_top_4, name = 'trending_top4'),
path('homepage_body/<slug:slug>/', homepage_body.as_view(), name = 'homepage_body'),
path('writer_of_week/',views.writer_of_week, name = 'writer_of_week'),

]
