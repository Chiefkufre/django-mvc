import random
from datetime import datetime
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify


# Internal imports
from .utils import ModelManager

from django.conf import settings

User = settings.AUTH_USER_MODEL

# implementing model managers

# class ArticleManager(models.Manager):
#     def search(self, query, **kwargs):
#         lookup = Q(title__icontains=query) | Q(content__icontains=query)
#         return self.get_queryset().filter(lookup).order_by('created')
# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    pub_date = models.DateTimeField()


    objects = ModelManager()
    def get_absolute_url(self):
        return f"/article/{self.slug}"
        # return reverse('article-detail')

    # def save(self, *args, **kwargs):

    #     if self.slug is None:
    #         self.slug = slugify(self.title)
        
    #     super().save(*args, **kwargs)


def slugify_instance_title(instance, save=False, new_slug=None):

    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    klass = instance.__class__
    qs = klass.object.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        rand_int = random.randint(300_000, 500_000)
        slug = f"{slug}-{rand_int}"
        return slugify_instance_title(instance, save=False, new_slug=None)
      
    instance.slug = slug
    if save:
        instance.save()
    return instance

def article_pre_save(sender, instance, *args, **kwargs):

    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(article_pre_save, sender=Article)


def article_post_save(sender, instance, created, *args, **kwargs):

    if created:
        slugify_instance_title(instance, save=True)

post_save.connect( article_post_save, sender=Article)



def article_content_post_save(sender, created, instance, *args, **kwargs):

    if created:
        slug = slugify(instance.content)
        instance.slug = slug
        instance.save()

post_save.connect(article_content_post_save, sender=Article)