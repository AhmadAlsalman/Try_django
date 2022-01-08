from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=120)
    content=models.CharField(max_length=120)
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    slug=models.SlugField(blank=True, null=True)


    def save(self,*args, **kwargs ):
        #this function mean : 
        #obj=Article.objects.get(id=1)
        #set something
        #if self.slug is None:
            #self.slug=slugify(self.title)
        super().save(*args, **kwargs)
        #obj.save()
        #do another something 

def slugify_instance_title(instance, save=False):
    slug=slugify(instance.title)
    qs=Article.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        slug=f"{slug}-{qs.count()+1}"
    instance.slug=slug
    if save:
        instance.save()
    return instance


def article_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance, save=False)
pre_save.connect(article_pre_save, sender=Article)


def article_post_save(sender, instance,created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)
post_save.connect(article_post_save, sender=Article)
