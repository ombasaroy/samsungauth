from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.


def index(request):
    users = User.objects.all().count()
    context = {'users': users}
    return render(request, 'index.html', context)


def loginform(request):
    return render(request, 'login.html')


def signupform(request):
    return render(request, 'signup.html')


def signupaction(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        signup = User.objects.create_user(username, password)
        signup.save()

        messages.success(request, 'Registration successful')
        return redirect('loginform')

    return render(request, 'signup.html')


def loginaction(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            messages.error(request, "Login failed.")
            return redirect('loginform')

    return render(request, 'login.html')
