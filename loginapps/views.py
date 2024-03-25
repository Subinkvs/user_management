from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login,logout





# Create your views here.



def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    return redirect('login')


def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return redirect('signup')

    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(username, email, password)
        myuser.save()

        return redirect('login')

    return render(request, "signup.html")


def logout(request):
    if request.user.is_authenticated:
        request.session.flush()
      
    return redirect('login')
