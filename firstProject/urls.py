"""
URL configuration for firstProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstProject import views
from AuthModel import views as authModelView
from BlogModel import views as blogModelView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.homePage),

    
    path('blogs/', blogModelView.blogs, name='blogs'),
    path('blogs/<slug_title>', blogModelView.Blog_Detail),
    path('my-blogs/<slug_title>', blogModelView.Edit_Blog),
    path('delete-blog/<slug_title>', blogModelView.Delete_Blog),
    path('my-blogs/', blogModelView.My_Blogs, name='my-blogs'),
    path('create-blog/', blogModelView.Create_Blog, name='create-blog'),
    

    path('contact-us/', views.contactPage, name= 'submitquery'),
    

    path('login/', authModelView.login_page, name='login'),
    path('register/', authModelView.register_page, name='register'),
    path('logout/', authModelView.logout_page),
    
]
