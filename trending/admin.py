from django.contrib import admin
from trending.models import Trending,trending_top1,trending_top2,trending_top3,trending_top4

admin.site.register(Trending)
admin.site.register(trending_top1)
admin.site.register(trending_top2)
admin.site.register(trending_top3)
admin.site.register(trending_top4)