from django.shortcuts import render
from .models import Politics
from . import models
from hitcount.views import HitCountDetailView



#This is politics page
def politics_list(request):
    title           = Politics.objects.first()
    top_3           = Politics.objects.all()[:7]
    context         = {'top_3':top_3,'title':title}
    return render (request, 'politics/politics_list.html',context)


class politics_detail(HitCountDetailView):
    model                   = models.Politics
    context_object_name     = 'politics_detail'
    template_name           = 'politics/politics_detail.html'
    slug_field              = 'slug'
    count_hit               = True

#***********************************END*************************************************************
