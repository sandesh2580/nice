from django.urls import path
from . import views
from Writers.views import view_writer
urlpatterns = [
    path('write/', views.writer, name= 'writers'),
    path('writer/<slug:slug>/', view_writer.as_view(), name = 'writer')

]
