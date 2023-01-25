from django.shortcuts import render,redirect
from django.conf import settings
#from gvpw.settings import STATICFILES_DIRS
from .models import face
import cv2,os
import numpy as np
from PIL import Image as im
from django.contrib import messages
from django.contrib.staticfiles.utils import get_files
from django.contrib.staticfiles.storage import StaticFilesStorage
from django.contrib.auth.models import User,auth
from accounts.models import MyUser
from django.templatetags.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.auth import authenticate, login, get_user_model
from django.core.files.storage import FileSystemStorage
import pandas as pd

# Create your views here.
def face_detection(request):
    if request.method=="POST":
        use = request.POST.get('use')
        pas = request.POST.get('pas')
        email = request.POST.get('email')
        file = request.FILES.get('file') 
        if pas=="faculty":
            MyUser.objects.create_user(username=use,password=pas,email=email,is_faculty=True).save()
            return render(request,'home/index.html')
        elif pas=="student":
            MyUser.objects.create_user(username=use,password=pas,email=email,is_student=True).save()
            return render(request,'home/index.html')
        else:
            messages.info(request,'change!')
            return render(request,'login/face_detection.html')
        
    return render(request,'login/face_detection.html')

def signin(request):
    if request.method=='POST':
        username=request.POST.get('use')
        password=request.POST.get('pas')
        user =auth.authenticate(username=username, password=password)
        pic=face.objects.filter(name=username,is_picsl=True).exists()
        cos=face.objects.filter(name=username,is_cosenger=True).exists()
        if user is not None:
            auth.login(request,user)
            if(request.user.is_faculty):
                return redirect('/')
            if(request.user.is_student):
                return redirect('/')
            if (pic):
                return redirect('/picsl/index/')
            if (cos):
                return redirect('/cosengers/')
            return redirect('/')
        else:
            messages.error(request,' invalid login, please try again. ')
            return redirect('/login/signin/')
    else:
        return render(request,'login/signin.html')
    return render(request,'login/signin.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
    
