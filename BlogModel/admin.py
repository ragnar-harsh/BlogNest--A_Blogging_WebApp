from django.contrib import admin
from BlogModel.models import BlogModel

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_desc', 'author','blog_img','title_slug','created_at','blog_view_count','blog_likes_count','author_name')

admin.site.register(BlogModel, BlogAdmin)