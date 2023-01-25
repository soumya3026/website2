from django.shortcuts import render
from home.models import Placement,News,Fac,Contact,acheivement
from accounts.models import MyUser 
from login.models import *
from faculty.models import *
from student.models import *
from django.contrib import messages
from qr_profile.models import *
import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.conf import settings
from django.apps import apps

import os
# Create your views here.
n=News.objects.order_by('-date')[:5]
staff=MyUser.objects.filter(is_staff=True)
def index(request):
    a = acheivement.objects.all()
    return render(request,'home/index.html',{'n':n,'a':a,'staff':staff})

def dept_abt(request):
    #n=News.objects.order_by('-date')[:5]
    return render(request,'home/dept_abt.html',{'n':n,'staff':staff})

def faculty(request):
    f = ProfFac.objects.all()
    #for i in f:
    #    print(i.pic)
    return render(request,'home/faculty.html',{'n':n,'f':f,'staff':staff})


def contact(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST.get('email',False)
        subject=request.POST['subject']
        msg=request.POST['msg']
        Contact(fname=fname,lname=lname,email=email,subject=subject,msg=msg).save()
        messages.info(request,'Message Sent!')
        return render(request,'home/contact.html')
    return render(request,'home/contact.html',{'n':n,'staff':staff})

def placements(request):
    p=Placement.objects.all()
    print(p)
    return render(request,'home/placements.html',{'p':p,'n':n,'staff':staff})

def add_placement(request):
    if request.method=="POST":
        url=request.POST['url']
        year=request.POST['year']
        Placement(url=url,year=year).save()
        return render(request,'home/placements.html')
    return render(request,'home/add_placement.html',{'n':n,'staff':staff})

def add_news(request):
    if request.method=="POST":
        url=request.POST['url']
        title=request.POST['title']
        date=request.POST['date']
        News(url=url,title=title,date=date).save()
        return render(request,'home/dept_abt.html')
    return render(request,'home/add_news.html',{'n':n,'staff':staff})

def add_faculty(request):
    if request.method=="POST":
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        email = request.POST.get('email')
        pic = request.FILES.get('pic')
        qualif = request.POST.get('qualif')
        resume = request.FILES.get('resume')
        Fac(name=name,designation=designation,email=email,pic=pic,qualif=qualif,resume=resume).save()
        return render(request,'home/add_faculty.html')
    return render(request,'home/add_faculty.html',{'n':n,'staff':staff})

def add_achievement(request):
    if request.method=="POST":
        name = request.POST.get('name')
        achieve = request.POST.get('achieve')
        pic = request.FILES.get('pic')
        acheivement(name=name,achieve=achieve,pic=pic).save()
        return render(request,'home/index.html')
    return render(request,'home/add_achievement.html',{'n':n,'staff':staff})

def adminst(request):
    return render(request,'home/adminst.html',{'n':n,'staff':staff})

def add_student(request):            
    try:
        if request.method == 'POST' and request.FILES['myfile']:     
            myfile = request.FILES['myfile']  
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            path = os.getcwd()
            k=str(os.path.abspath(os.path.join(path, os.pardir)))
            k=k.replace('\\','/')
            empexceldata = pd.read_excel(k+excel_file)
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():
                b=MyUser.objects.filter(username=dbframe.username).exists()
                if b==False:
                    obj = MyUser.objects.create_user(username=dbframe.username,first_name=dbframe.first_name,last_name=dbframe.last_name, email=dbframe.email,is_staff=dbframe.is_staff,is_student=dbframe.is_student,is_faculty=dbframe.is_faculty,password=dbframe.password)
                    obj.save()
                    if dbframe.is_student == True:
                        student_profile(uname=dbframe.username,year=dbframe.year,sem=dbframe.sem,done='0').save()
                MyUser.objects.filter(username=dbframe.username).update(first_name=dbframe.first_name,last_name=dbframe.last_name, email=dbframe.email,is_staff=dbframe.is_staff,is_student=dbframe.is_student,is_faculty=dbframe.is_faculty)
            return render(request, 'home/add_student.html', {
                'uploaded_file_url': uploaded_file_url
            })    
    except Exception as identifier:            
        print(identifier)
     
    return render(request, 'home/add_student.html',{})

def delete_fac(request,pk):
    if request.method=='POST':
        fac=Fac.objects.get(pk=pk)
        print(faculty)
        fac.delete()
        f = Fac.objects.all()
    #for i in f:
    #    print(i.pic)
    return render(request,'home/faculty.html',{'n':n,'f':f,'staff':staff})

def team(request):
    return render(request,'home/team.html',{'n':n})

def resum(request,pk):
    return render(request,'home/resum.html',{'n':n})