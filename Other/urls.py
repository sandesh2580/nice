from django.urls import path
from . import views
from . views import others_list,others_detail

urlpatterns = [
    path('others/', views.others_list , name = 'others'),
    path('others_detail/<slug:slug>/', others_detail.as_view(), name = 'others_detail')
    
]