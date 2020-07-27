from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation

class writers(models.Model):
    TOPICS = (
        ('Politics','Politics'),
        ('Science and Technology', 'Science and Technology'),
        ('Sports','Sports'),
        ('Health', 'Health')
    )
    name            = models.CharField(max_length=20, null= True)
    topics          = models.CharField(max_length=30,null= True,choices=TOPICS)
    image           = models.ImageField(null = True , upload_to = 'writers')
    soeciality      = models.CharField(null=True,max_length=20)
    slug            = models.SlugField(max_length=100, null=True,blank=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk')

    def __str__(self):
        return self.name

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    slug        = slugify(instance.name)
    exist       = writers.objects.filter(slug = slug).exists()
    if exist:
        slug    = "%s-%s" %(slug, instance.id)
    
    instance.slug   = slug


pre_save.connect(pre_save_post_receiver, sender = writers)

