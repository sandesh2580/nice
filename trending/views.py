from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from . import models
from hitcount.views import HitCountDetailView
from .models import Trending,trending_top1,trending_top2,trending_top3,trending_top4

#/This is first topics in trending/
def trending_top_1(request):
    title               = trending_top1.objects.first()
    top_3               = trending_top1.objects.all().order_by('-date_posted')[:3]
    context             = {'title':title,'top_3':top_3}
    return render (request , 'trending/trending_top1.html',context)

class trending_top1_detail(HitCountDetailView):
    model                   = models.trending_top1
    context_object_name     = 'trending_top1'
    template_name           = 'trending/trending_top1_detail.html'
    slug_field              = 'slug'
    count_hit               = True
#/***********************END ***************************************/

#/This is second topics in trending/
def trending_top_2(request):
    title               = trending_top2.objects.first()
    top_3               = trending_top2 .objects.all().order_by('-date_posted')[:3]
    context             = {'title':title,'top_3':top_3}
    return render (request , 'trending/trending_top2.html',context)
class trending_top2_detail(HitCountDetailView):
    model                   = models.trending_top2
    context_object_name     = 'trending_top2'
    template_name           = 'trending/trending_top2_detail.html'
    slug_field              = 'slug'
    count_hit               = True

#/***********************END ***************************************/

#/This is third topics in trending/
def trending_top_3(request):
    title               = trending_top3.objects.first()
    top_3               = trending_top3.objects.all()[:3]
    context             = {'title':title,'top_3':top_3}
    return render (request , 'trending/trending_top3.html',context)
class trending_top3_detail(DetailView):
    model                   = models.trending_top2
    context_object_name     = 'trending_top3'
    template_name           = 'trending/trending_top3_detail.html'
    slug_field              = 'slug'

#/***********************END ***************************************/

#/This is fourth topics in trending/
def trending_top_4(request):
    title               = trending_top4.objects.first()
    top_3               = trending_top4.objects.all()[:3]
    context             = {'title':title,'top_3':top_3}
    return render (request , 'trending/trending_top4.html',context)
class trending_top4_detail(DetailView):
    model                   = models.trending_top4
    context_object_name     = 'trending_top4'
    template_name           = 'trending/trending_top4_detail.html'
    slug_field              = 'slug'

#/***********************END ***************************************/



#This is for top objects in homepage
def Trending_page(request):
    top3 = Trending.objects.all()[:3]
    context = {'trending_page':top3}
    return render (request, 'trending/trending_page.html',context)

class Trending_detail(HitCountDetailView):
    model                       = models.Trending
    context_object_name         = 'trending_detail'
    template_name               = 'trending/trending_detail.html'
    slug_field                  =  'slug'
    count_hit                   = True
#/***********************END ***************************************/

