from django.db import models
from django.contrib.auth.models import User
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models.signals import pre_save
from django.utils.text import slugify
class Trending(models.Model):
    TOPICS = (
        ('Corona' , 'Corona'),
        ('Border', 'Border'),
        ('Kp Oli', 'Kp Oli'),
        ('Locust Attack', 'Locust Attack'),
    )
    title           = models.CharField(max_length=15, null = True,choices=TOPICS)
    author          = models.ForeignKey(User, on_delete= models.CASCADE, null= True)
    post_title      = models.CharField(max_length=55, null=True)
    paragraph1      = models.TextField(blank=False, null= True)
    date_posted     = models.DateTimeField(auto_now_add=True,auto_now = False,null=True)
    image           = models.ImageField(null = True, upload_to = 'trending_pics')
    paragraph2      = models.TextField(null=True)
    slug            = models.SlugField(null = True, max_length=1000, blank = True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk')
    def __str__(self):
        return self.title

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    slug        = slugify(instance.post_title)
    exist       = Trending.objects.filter(slug = slug).exists()
    if exist:
        slug    = "%s-%s" %(slug, instance.id)
    
    instance.slug   = slug


pre_save.connect(pre_save_post_receiver, sender = Trending)


class trending_top1(models.Model):
 
    AUTHORS =(
        ('Sandesh','Sandesh'),
        ('Binod', 'Binod'),
        ('Manasi', 'Manasi'),
    )
    title           = models.ForeignKey(Trending, on_delete = models.CASCADE, null =  True)
    author          = models.CharField(max_length=15,null=True,choices=AUTHORS)
    post_title      = models.CharField(max_length=55, null=True)
    paragraph1      = models.TextField(blank=False, null= True)
    date_posted     = models.DateTimeField(auto_now_add=True,auto_now = False,null=True)
    image           = models.ImageField(null = True, upload_to = 'trending_pics')
    paragraph2      = models.TextField(null=True)
    slug            = models.SlugField(null = True, max_length=10, blank = True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk')
    def __str__(self):
        return self.post_title

class trending_top2(models.Model):
    title           = models.CharField(max_length=15, null = True)
    author          = models.ForeignKey(User, on_delete= models.CASCADE, null= True)
    post_title      = models.CharField(max_length=55, null=True)
    paragraph1      = models.TextField(blank=False, null= True)
    date_posted     = models.DateTimeField(auto_now_add=True,auto_now = False,null=True)
    image           = models.ImageField(null = True, upload_to = 'trending_pics')
    paragraph2      = models.TextField(null=True)
    slug            = models.SlugField(null = True, max_length=10, blank = True)

    def __str__(self):
        return self.post_title

class trending_top3(models.Model):
    title           = models.CharField(max_length=15, null = True)
    author          = models.ForeignKey(User, on_delete= models.CASCADE, null= True)
    post_title      = models.CharField(max_length=55, null=True)
    paragraph1      = models.TextField(blank=False, null= True)
    date_posted     = models.DateTimeField(auto_now_add=True,auto_now = False,null=True)
    image           = models.ImageField(null = True, upload_to = 'trending_pics')
    paragraph2      = models.TextField(null=True)
    slug            = models.SlugField(null = True, max_length=10, blank = True)
    def __str__(self):
        return self.post_title
class trending_top4(models.Model):
    title           = models.CharField(max_length=15, null = True)
    author          = models.ForeignKey(User, on_delete= models.CASCADE, null= True)
    post_title      = models.CharField(max_length=55, null=True)
    paragraph1      = models.TextField(blank=False, null= True)
    date_posted     = models.DateTimeField(auto_now_add=True,auto_now = False,null=True)
    image           = models.ImageField(null = True, upload_to = 'trending_pics')
    paragraph2      = models.TextField(null=True)
    slug            = models.SlugField(null = True, max_length=10, blank = True)
    def __str__(self):
        return self.post_title
