from django.shortcuts import render, redirect
from BlogModel.models import BlogModel
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator


@login_required(login_url='/login')
def Create_Blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        author_name = request.user.get_full_name()
        BlogModel.objects.create(
            blog_title = title,
            blog_img = image,
            blog_desc = description,
            author = request.user,
            author_name = author_name
        )
        messages.success(request, "Blog created")
        return redirect('/my-blogs')

    return render(request, "createBlog.html")
# Create your views here.


@login_required(login_url='/login/')
def blogs(request):
    blogs = BlogModel.objects.all().order_by('-blog_view_count')
    
    if request.method == 'GET':
        search_item = request.GET.get('search')
        if search_item is not None:
            blogs = BlogModel.objects.filter(blog_title__icontains = search_item)

    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    paged_blog = paginator.get_page(page_number)
    total_page = paged_blog.paginator.num_pages

    data = {
        'top3': blogs[0:3],
        'otherBlogs': paged_blog,
        'total_pages' : [n+1 for n in range(total_page)]
    }

    return render(request, "blogs.html", data)



@login_required(login_url='/login/')
def Blog_Detail(request, slug_title):
    curr_blog = BlogModel.objects.get(title_slug = slug_title)
    curr_blog.blog_view_count += 1
    curr_blog.save()

    print(request.user.get_full_name())

    # print(User.objects.get(username = curr_blog.author).get_full_name())
    return render(request, "blogDesc.html", { 'curr_blog' : curr_blog })



@login_required(login_url='/login/')
def My_Blogs(request):
    blogs = BlogModel.objects.filter(author = request.user).order_by('-blog_view_count')

    if request.method == 'GET':
        search_item = request.GET.get('search')
        if search_item is not None:
            blogs = BlogModel.objects.filter(blog_title__icontains = search_item)

    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    paged_blog = paginator.get_page(page_number)
    total_pages = paged_blog.paginator.num_pages

    data = {
        'top3': blogs[0:3],
        'otherBlogs': paged_blog,
        'total_pages': [n+1 for n in range(total_pages)]
    }

    return render(request, "myBlogs.html", data)

@login_required(login_url='/login/')
def Edit_Blog(request, slug_title):
    curr_blog = BlogModel.objects.get(title_slug = slug_title)
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('description')
        img = request.FILES.get('image')

        curr_blog.blog_title = title
        curr_blog.blog_desc = desc
        curr_blog.blog_img = img
        curr_blog.save()
        messages.info(request, "Blog Updated")
        
        return redirect('/my-blogs')

    print(curr_blog.blog_title)
    
    return render(request, "EditBlog.html", { 'curr_blog' : curr_blog })


def Delete_Blog(request, slug_title):
    curr_blog = BlogModel.objects.get(title_slug = slug_title)
    if curr_blog is not None:
        curr_blog.delete()
        messages.info(request, "Blog Deleted")
        return redirect('my-blogs')