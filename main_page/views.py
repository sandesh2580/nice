from django.shortcuts import render
from . import models
from .models import trending_top,body_block,writer_of_week
from django.views.generic import View,TemplateView,ListView,DetailView
from hitcount.views import HitCountDetailView
from politics.models import Politics 
from   Writers.models import writers


# This is list of the trending
def homepage(request):
    title           = trending_top.objects.first()
    second          = trending_top.objects.get(id=2)
    third           = trending_top.objects.get(id=3)
    fourth          = trending_top.objects.get(id=4)
    homepage_body   = body_block.objects.first()
    top_6           = body_block.objects.all()[1:7]
    politics        = Politics.objects.all()[:3]
    w_top3         = writers.objects.all()[1:4]
    context         = {'title':title, 'second':second, 'third':third,'fourth':fourth,'top_6':homepage_body,'top':top_6,'top_3':politics,'writers':w_top3}
    return render (request, 'main_page/homepage.html',context)
#***********************************END*************************************************************

# This is body block 
class homepage_body(HitCountDetailView): 
    model                       = models.body_block
    context_object_name         = 'homepage_body'
    template_name               = 'main_page/homepage_body.html'
    slug_field                  = 'slug'
    count_hit                   = True
#***********************************END*************************************************************


def writer_of_week(request):
    top_writer           = writer.objects.all()
    context             =  {'top_writer':top_writer}
    
    return render(request, 'main_page/writer_of_week.html',context)

