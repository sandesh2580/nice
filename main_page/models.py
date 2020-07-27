from django.db import models
from django.contrib.auth.models import User 
from trending.models import Trending
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models.signals import pre_save
from django.utils.text import slugify

class trending_top(models.Model):
    title           = models.ForeignKey(Trending,on_delete = models.CASCADE, null=True)

class body_block(models.Model):
    CATEGORY    = (
        ('Politics', 'Politics'),
        ('Health', 'Health'),
        ('Sports', 'Sports'),
        ('Others', 'Others'),

    )
    title           = models.CharField(max_length=15, null = True, choices=CATEGORY)
    author          = models.ForeignKey(User, on_delete= models.CASCADE, null= True)
    post_title      = models.CharField(max_length=55, null=True)
    paragraph1      = models.TextField(blank=False, null= True)
    date_posted     = models.DateTimeField(auto_now_add=True,auto_now = False,null=True)
    image           = models.ImageField(null = True, upload_to = 'bodyblock_pics')
    paragraph2      = models.TextField(null=True)
    slug            = models.SlugField(null = True, max_length=10, blank = True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk')
    def __str__(self):
        return self.post_title
    

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    slug        = slugify(instance.post_title)
    exist       = body_block.objects.filter(slug = slug).exists()
    if exist:
        slug    = "%s-%s" %(slug, instance.id)
    
    instance.slug   = slug


pre_save.connect(pre_save_post_receiver, sender = body_block)


class writer_of_week(models.Model):
    TOPICS = (
        ('Politics','Politics'),
        ('Science and Technology', 'Science and Technology'),
        ('Sports','Sports'),
        ('Health', 'Health')
    )
    name            = models.CharField(max_length=20, null= True)
    topics          = models.CharField(max_length=30,null= True,choices=TOPICS)
    image           = models.ImageField(null = True , upload_to = 'writer_of_week')
    soeciality      = models.CharField(null=True,max_length=20)
    slug            = models.SlugField(max_length=100, null=True,blank=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk')

    def __str__(self):
        return self.name
