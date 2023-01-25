from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
import re
import qrcode
import os,os.path
import requests
from django.contrib.auth.models import User,auth
from home.models import Fac
from .models import Detail,Degree,Exam,Appeared,Photo, ProfFac
from accounts.models import MyUser
from qrcode import *
import cloudinary
import cloudinary.uploader
import cloudinary.api
# Create your views here.
#def index(request):
#    return render(request,'qr_profile/index.html')


def detail(request):
    data = request.user
    p=''
    profile = ''
    pro2 = ''
    #print(profile.qualif)
    if str(data) == "admin":
        #print("yy")
        h = Photo.objects.all()
        l=[i.use for i in h]
        k=[]
        m=[]
        for i in l:
            for j in h:
                if i not in m and i==j.use:
                    k.append(j)
                    m.append(i)
        return render(request,'qr_profile/detail.html',{'k':k})
    elif data.is_faculty:
        pro2 = ProfFac.objects.get(email=request.user.email)
    if Photo.objects.filter(use=data.username).exists():
        p = MyUser.objects.get(username=data.username)
        photo = Photo.objects.all()
        l=[]
        for i in photo:
            if i.use==data.username:
                l.append(i)
        return render(request,'qr_profile/detail.html',{'p':p,'profile':profile,'p':p,'l':l})
    return render(request,'qr_profile/detail.html',{'profile':profile,'p':p,'pro2':pro2})
 
def upload(request):
    #q = Detail.objects.last()
    if request.user.is_faculty:
        e = Degree.objects.get(deg="Faculty")
    else:
        e = Degree.objects.get(deg="Student")
    if request.method=="POST":
        if request.POST.get('enam'):
            savedata = Appeared()
            savedata.enam=request.POST.get('enam')
            savedata.nam=request.user.username
            savedata.save()
            return render(request,'qr_profile/upload.html',{'e':e})
    else:
        return render(request,'qr_profile/upload.html',{'e':e})
    return render(request,'qr_profile/upload.html',{'e':e})



def select(request):
    p=Appeared.objects.last()
    m=p.enam.split(",")
    l=[]
    for i in m:
        if i!="":
            l.append(i)
    for i in l:
        if request.method=="POST":
            i = request.FILES.get(i)
            Photo(use=request.user.username,title=i,image=i).save()
    return render(request,'qr_profile/select.html',{'l':l})


def quick(request):
    data = request.user
    photo = Photo.objects.all()
    l=[]
    q={}
    for i in photo:
        if i.use==data.username:
            l.append(i)
            q[i.title]=i.image.url 
    print(q)
    #with open("static/qr_profile/"+data.username+".png",'w') as f:
    img = make(q)
    img.save("static/qr_profile/"+data.username+".png")
    return render(request,'qr_profile/quick.html',{'data':data,'photo':photo,'l':l})

def gen(request):
    data = request.user.username
    p = MyUser.objects.get(username=data)
    return render(request,'qr_profile/gen.html',{'p':p,'data':data})


def delete(request):
    data = request.user
    photo = Photo.objects.all()
    l=[]
    q={}
    m=[]
    for i in photo:
        if i.use==data.username:
            l.append(i)
            q[i.title]=i.image.url
            #Photo.objects.get(i.id).delete()
            #cloudinary.uploader.destroy(i.image.public_id,invalidate=True)
            m.append(i.id)  
    return HttpResponse("deleted")


def upd(request):
    data = request.user
    photo = Photo.objects.all()
    l=[]
    q={}
    for i in photo:
        if i.use==data.username:
            l.append(i)
            q[i.title]=i.image.url
    return render(request,'qr_profile/upd.html',{'data':data,'photo':photo,'l':l})

def disp(request,pk):
    q = Photo.objects.get(pk=pk)
    photo = Photo.objects.all()
    l=[]
    #q={}
    for i in photo:
        if i.use==q.use:
            l.append(i)
    #        q[i.title]=i.image.url
    print(q)
    return render(request,'qr_profile/disp.html',{'l':l,'q':q.use})

def resum(request,pk):
    res=""
    r = ""
    if request.method=="POST":
        r = ProfFac.objects.get(pk=pk)
        #print(res.email)
        res = ProfFac.objects.get(email=r.email)
    return render(request,'qr_profile/resum.html',{'res':res,'r':r})

def del_doc(request,pk):
    if request.method=='POST':
        event=Photo.objects.get(pk=pk)
        event.delete()
    #return render(request,'cosengers/reg_evn.html',{'q':q})

    return render(request,'qr_profile/detail.html')
   
   