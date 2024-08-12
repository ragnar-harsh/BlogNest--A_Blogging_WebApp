from django.contrib import admin
from blogs.models import BlogModel

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_desc')

admin.site.register(BlogModel, BlogAdmin)

# Register your models here.
