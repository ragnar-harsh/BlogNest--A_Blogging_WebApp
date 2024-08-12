from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def login_page(request):
    data = {
        'title': "Login | Register",
        'css' : "login.css"
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username = email)
        if not user.exists():
            messages.info(request, "User is not registered !")
            return redirect('/login/')
        else:
            user = authenticate(username = email, password = password)
            if user is None:
                messages.error(request, "Invalid Password")
                return redirect('/login')
            else:
                # messages.info(request, "Login Successfull")
                login(request, user)
                return redirect('/blogs')

    return render(request, 'login.html', data)



def register_page(request):

    data = {
        'title': "Login | Register",
        'css' : "login.css"
    }

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confPassword = request.POST.get('confirm-password')

        user = User.objects.filter(username = email)
        if user.exists():
            messages.info(request, "User is already registered")
            return redirect('/register/')

        if password == confPassword:
            user = User.objects.create(
                first_name = fname,
                last_name = lname,
                username = email,
                )
            user.set_password(password)
            user.save()
            messages.info(request, "Account created Successfully")
            return redirect('/register/')
        else:
            messages.info(request, "Password does not match")
            return redirect('/register/')
    
    return render(request, 'register.html', data)


def logout_page(request):
    messages.success(request, "Logged Out Successfully")
    logout(request)
    return redirect('/login')