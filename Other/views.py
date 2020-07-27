from django.shortcuts import render
from .models import Others
from . import models
from hitcount.views import HitCountDetailView



#This is Others page
def others_list(request):
    top_3           = Others.objects.all()[:3]
    context         = {'top_3':top_3}
    return render (request, 'Other/other_list.html',context)


class others_detail(HitCountDetailView):
    model                   = models.Others
    context_object_name     = 'others_detail'
    template_name           = 'Other/other_detail.html'
    slug_field              = 'slug'
    count_hit               = True

#***********************************END*************************************************************
