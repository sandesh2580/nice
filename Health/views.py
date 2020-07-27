from django.shortcuts import render
from . import models
from .models import Health
from hitcount.views import HitCountDetailView

#This is healthy page
def health_list(request):
    top_3           = Health.objects.all()[:4]
    context         = {'top_3':top_3}
    return render (request, 'Health/health_list.html',context)
    
class health_detail(HitCountDetailView):
    model                   = models.Health
    context_object_name     = 'health_detail'
    template_name           = 'Health/health_detail.html'
    slug_field              = 'slug'
    count_hit               = True


#***********************************END*************************************************************





