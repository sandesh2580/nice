from django.urls import path
from . import views
from . views import health_list,health_detail
urlpatterns = [
    path('health/', views.health_list , name = 'health'),
    path('health_detail/<slug:slug>/', health_detail.as_view(), name = 'health_detail')
    
]