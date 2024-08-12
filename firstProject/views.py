from django.http import HttpResponse
from django.shortcuts import render
from service.models import Service
from contactModel.models import contactModel
from blogs.models import BlogModel
from django.core.paginator import Paginator
from django.core import paginator
from django.contrib.auth.decorators import login_required


def homePage(request):
    features = Service.objects.all()
    if request.method == 'GET':
        search = request.GET.get('search')
        if search != None:
            features = Service.objects.filter(service_title__icontains = search)
    data = {
        'title' : "Home Page",
        'heading': "Welcome to Home Page",
        'courses': ['PHP', 'Java', 'Python', 'Angular'],
        'features': features,
        'css': 'nav.css',
    }
    return render(request, "index.html", data)


@login_required(login_url='/login/')
def blogs(request):
    blogs = BlogModel.objects.all()

    data = {
        'top3': blogs[0:3],
        'otherBlogs': blogs
    }

    return render(request, "blogs.html", data)


def contactPage(request):
    res = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        query = contactModel(name=name, email= email, message = message)
        query.save()
        res = "Contact Message Submitted "
    return render(request, "contact.html", {'res' : res})


def courses(request):
    return HttpResponse("<i>Welcome to First Course</i>")


def courseDetail(request, courseid):
    return HttpResponse(courseid)


def blogDetail(request, slug_title):
    curr_blog = BlogModel.objects.get(title_slug = slug_title)
    print(curr_blog.blog_title)
    return render(request, "blogDesc.html", { 'curr_blog' : curr_blog })
