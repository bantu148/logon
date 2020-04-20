from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def alogin(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return render(request, 'after_login.html')

    else:
        return render(request, 'register.html')



def new(request):
    email = request.POST.get("email")
    username = request.POST.get("username")
    password1 = request.POST.get("password1")
    password2 = request.POST.get("password2")

    params = {'email': email}
    user = User.objects.create_user(username=username, email=email, password=password1)
    user.save()

    return render(request, "new.html", params)