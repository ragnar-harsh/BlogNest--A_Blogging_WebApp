from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class BlogModel(models.Model):
    # blog_img = models.CharField(max_length=100)
    blog_title = models.CharField(max_length=100)
    blog_desc = HTMLField()
    title_slug = AutoSlugField(populate_from= 'blog_title', unique=True, null=True, default=None)
# Create your models here.
