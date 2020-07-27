from django.urls import path
from .views import politics_list,politics_detail
from . import views
urlpatterns = [

    path('politics/', views.politics_list, name = 'politic'),
    path('politics_detail/<slug:slug>/', politics_detail.as_view(), name = 'politics_detail'),

    
]
