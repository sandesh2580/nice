from django.shortcuts import render
from . import models
from .models import writers
from hitcount.views import HitCountDetailView

def  writer(request):
    writer         = writers.objects.all()
  
    top_writer      = writers.objects.filter(slug = 'manasi-acharya')
    context         = {'writers':writer,'top_writer':top_writer}
    return render(request, 'Writers/writers.html',context)



class view_writer(HitCountDetailView):
    model                   = writers
    template_name           = 'Writers/view_writer.html'
    context_object_name     = 'writer'
    slug                    = 'slug'
    hit_count               = True

