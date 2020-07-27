from django.shortcuts import render
from .models import Sport
from . import models
from hitcount.views import HitCountDetailView



#This is sports page
def sports_list(request):
    top_3           = Sport.objects.all()[:3]
    context         = {'top_3':top_3}
    return render (request, 'Sports/sports_list.html',context)


class sports_detail(HitCountDetailView):
    model                   = models.Sport
    context_object_name     = 'sports_detail'
    template_name           = 'Sports/sports_detail.html'
    slug_field              = 'slug'
    count_hit               = True

#***********************************END*************************************************************

