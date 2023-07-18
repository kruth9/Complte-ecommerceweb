from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import*
# Create your views here.
def Home(request):
    data=Items.objects.all()
    return render(request, 'home.html', {'data': data})
   

def Developers(request):
    return render (request,"developers.html")

def Boys(request):
    list=Secitems.objects.all()
    return render (request,"BOYS.html",{'list':list})


def Womens(request):
    wec=Wecitems.objects.all()
    return render (request,"women.html",{'wec':wec})


def cart(request):
    
    return render(request, 'cart.html')

def Collections(request):
    cec=cecitems.objects.all()
    fec=fecitems.objects.all()
    return render (request,"collection.html",{'cec': cec, 'fec': fec})


def Account(request):
    return render (request,"Account.html")
