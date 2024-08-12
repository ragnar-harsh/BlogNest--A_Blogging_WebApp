from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.utils import timezone

class BlogModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_img = models.ImageField(upload_to="static/images/", blank=False, null=False)
    blog_title = models.CharField(max_length=200)
    blog_desc = HTMLField()
    title_slug = AutoSlugField(populate_from= 'blog_title', unique=True, null=True, default=None)
    created_at = models.DateTimeField(default=timezone.now)
    blog_view_count = models.IntegerField(default=1)
    blog_likes_count = models.IntegerField(default=0)
    author_name = models.CharField(max_length=50, null=True)
# Create your models here.