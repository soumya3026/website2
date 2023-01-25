from accounts.models import MyUser
from .models import nevents, blog, eventdetails
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
import os
from .forms import neventsForm,nblogsForm
from login.models import face

# Create your views here.
def about_us(request):
    pic=False
    if request.user.is_authenticated:
        pic=face.objects.filter(name=request.user.username,is_picsl=True).exists()
    return render(request,'picsl/about_us.html',{'pic':pic})
def blogs(request):
    nblog=blog.objects.all()[:2]
    pic=False
    if request.user.is_authenticated:
        pic=face.objects.filter(name=request.user.username,is_picsl=True).exists()
    return render(request,'picsl/blogs.html',{'nblog':nblog,'pic':pic})
def index(request):
    #nblog=blog.objects.all()
    #nevent=nevents.objects.all()[:3]
    evnt = eventdetails.objects.all()
    pic=False
    if request.user.is_authenticated:
        pic=face.objects.filter(name=request.user.username,is_picsl=True).exists()
    return render(request,'picsl/index.html',{'evnt':evnt,'pic':pic})
def events(request):
    nevent=nevents.objects.all()
    pic=False
    if request.user.is_authenticated:
        pic=face.objects.filter(name=request.user.username,is_picsl=True).exists()
    return render(request,'picsl/events.html',{'nevent':nevent,'pic':pic})


def abt_evn(request,pk):
    pic=False
    if request.user.is_authenticated:
        pic=face.objects.filter(name=request.user.username,is_picsl=True).exists()
    if request.method=="POST":
        evnt = eventdetails.objects.get(pk=pk)
    return render(request,'picsl/abt_evn.html',{'evnt':evnt,'pic':pic})
    
def upload_events(request):
    pic=False
    if request.method=='POST':
        form=neventsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        if request.user.is_authenticated:
            pic=face.objects.filter(name=request.user.username,is_picsl=True).exists()
    else:   
        if request.user.is_authenticated:
            pic=face.objects.filter(name=request.user.username,is_picsl=True).exists()
            form=neventsForm()
    return render(request,'picsl/upload_events.html',{'form':form,'pic':pic})

def add_evn(request):
    pic=False
    if request.user.is_authenticated:
            pic=face.objects.filter(name=request.user.username,is_picsl=True).exists()
    if request.method=="POST":
        title = request.POST.get('title')
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        desc = request.POST.get('desc')
        img1 = request.FILES.get('img1')
        img2 = request.FILES.get('img2')
        img3 = request.FILES.get('img3')
        eventdetails(title=title,fromdate=fromdate,todate=todate,desc=desc,img1=img1,img2=img2,img3=img3).save()
    return render(request,'picsl/add_evn.html',{'pic':pic})


def delete_blogs(request,pk):
    if request.method=='POST':
        blogs=blog.objects.get(pk=pk)
        blogs.delete()
    return render(request,'picsl/index.html')

def del_eve(request,pk):
    if request.method=='POST':
        eve=eventdetails.objects.get(pk=pk)
        eve.delete()
    return render(request,'picsl/index.html')

def delete_events(request,pk):
    if request.method=='POST':
        event=nevents.objects.get(pk=pk)
        event.delete()
    return render(request,'picsl/index.html')



def upload_blogs(request):
    if request.method=='POST':
        form=nblogsForm(request.POST,request.FILES)
        if form.is_valid():
           form.save()
        if request.user.is_authenticated:
            pic=face.objects.filter(name=request.user.username,is_picsl=True).exists()
    else:
        if request.user.is_authenticated:
            pic=face.objects.filter(name=request.user.username,is_picsl=True).exists()
            form=nblogsForm()

    return render(request,'picsl/upload_blogs.html',{'form':form,'pic':pic})

