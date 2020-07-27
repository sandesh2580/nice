from django.urls import path
from . import views
from . views import sports_list,sports_detail

urlpatterns = [
    path('sports/', views.sports_list , name = 'sports'),
    path('sports_detail/<slug:slug>/', sports_detail.as_view(), name = 'sports_detail')
    
]