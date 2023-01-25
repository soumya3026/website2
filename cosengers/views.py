from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.utils import timezone
#from app.models import Destination
from django.http import HttpResponse
from .forms import  *
from .models import  *
from cosengers.models import *
from login.models import *
#from django.models import forms
#from django.forms import DestinationForm
# Create your views here.
def index(request):
    q=False
    if request.user.is_authenticated:
        q=face.objects.filter(name=request.user.username,is_cosenger=True).exists()
    o = Event.objects.order_by('-date')
    return render(request,"cosengers/index.html",{'q':q,'o':o})

def add(request):
    q=False
    if request.user.is_authenticated:
        q=face.objects.filter(name=request.user.username,is_cosenger=True).exists()
    if request.method=="POST":
        name = request.POST.get('name')
        date = request.POST.get('date')
        link = request.POST.get('link')
        desc = request.POST.get('desc')
        NewEvent(name=name,date=date,link=link,desc=desc).save()
    return render(request,'cosengers/add.html',{'q':q})

def event(request,pk):
    q=False
    if request.user.is_authenticated:
        q=face.objects.filter(name=request.user.username,is_cosenger=True).exists()
    event_detail=""
    if request.method=="POST":
        event_detail = Event.objects.get(pk=pk)
    o = Event.objects.all()
    return render(request,'cosengers/event.html',{'event_detail':event_detail,'o':o,'q':q})

def add_event(request):
    q=False
    if request.user.is_authenticated:
        q=face.objects.filter(name=request.user.username,is_cosenger=True).exists()
    if request.method=="POST":
        name = request.POST.get('name')
        date = request.POST.get('date')
        activity = request.POST.get('activity')
        res_person = request.POST.get('res_person')
        remarks = request.POST.get('remarks')
        img1 = request.FILES.get('img1')
        img2 = request.FILES.get('img2')
        img3 = request.FILES.get('img3')
        Event(name=name,date=date,activity=activity,res_persn=res_person,remarks=remarks,img1=img1,img2=img2,img3=img3).save()
    return render(request,'cosengers/add_event.html',{'q':q})

def about(request):
    q=False
    if request.user.is_authenticated:
        q=face.objects.filter(name=request.user.username,is_cosenger=True).exists()
    return render(request,'cosengers/about.html',{'q':q})

def reg_evn(request):
    event = NewEvent.objects.all()
    q=False
    if request.user.is_authenticated:
        q=face.objects.filter(name=request.user.username,is_cosenger=True).exists()
    return render(request,'cosengers/reg_evn.html',{'event':event,'q':q})

def del_event(request,pk):
    q=False
    if request.user.is_authenticated:
        q=face.objects.filter(name=request.user.username,is_cosenger=True).exists()
    if request.method=='POST':
        event=NewEvent.objects.get(pk=pk)
        event.delete()
    return render(request,'cosengers/reg_evn.html',{'q':q})

def blogs(request):
    q=False
    if request.user.is_authenticated:
        q=face.objects.filter(name=request.user.username,is_cosenger=True).exists()
    blog = NewBlog.objects.all()
    return render(request,'cosengers/blogs.html',{'blog':blog,'q':q})

def add_blog(request):
    q=False
    if request.user.is_authenticated:
        q=face.objects.filter(name=request.user.username,is_cosenger=True).exists()
    if request.method=="POST":
        title = request.POST.get('title')
        img = request.FILES.get('img')
        desc = request.POST.get('desc')
        NewBlog(title=title,img=img,desc=desc).save()
    return render(request,'cosengers/add_blog.html',{'q':q})

def del_blog(request,pk):
    q=False
    if request.user.is_authenticated:
        q=face.objects.filter(name=request.user.username,is_cosenger=True).exists()
    if request.method=='POST':
        blog=NewBlog.objects.get(pk=pk)
        blog.delete()
    return render(request,'cosengers/blogs.html',{'q':q})

def del_ev_det(request,pk):
    q = False
    if request.user.is_authenticated:
        q=face.objects.filter(name=request.user.username,is_cosenger=True).exists()
    if request.method=='POST':
        blog=Event.objects.get(pk=pk)
        blog.delete()
    return render(request,'cosengers/blogs.html',{'q':q})