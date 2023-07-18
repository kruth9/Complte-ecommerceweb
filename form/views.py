from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from django.http import HttpResponse,HttpResponseRedirect

from django.contrib.auth import authenticate, login,logout

from .models import*
import requests
from django.http import JsonResponse
from django.contrib import messages
import requests

def homepage(request):
    return HttpResponse('home page')

def contact(request):
    return render(request,"contact.html")

# sign in
# sign up
#logh ut

def handle_signin(request):
    if request.method=="POST":
        username=request.POST['loginusername']
        email=request.POST['email']
        password=request.POST['loginpassword']
        user=User.objects.create_user(username,email,password)
        user.save()
        return redirect('signin')
    return render(request,'signin.html')

def Handle_login(request):
    if request.method=='POST':
        username=request.POST['loginusername']
        password=request.POST['loginpassword']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('Home')
        else:
            return redirect('signin')
    return render(request,"login.html")


def Handle_logout(request):
    logout(request)
    return redirect('signin')