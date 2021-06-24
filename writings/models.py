from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from ideas.utils import unique_slug_generator

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Writing(models.Model):
    cover = models.ImageField(null=True, blank=True)
    headline = models.CharField(max_length=120,null=True,blank=True)
    main_author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    textarea = RichTextField(max_length=2000, null=True, blank=True)
    # text = models.TextField( max_length=2000, null=True, blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.headline

@receiver(pre_save,sender=Writing)
def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)