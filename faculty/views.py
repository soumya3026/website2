from django.shortcuts import render
from student.models import basic_3_1
from student.models import mid1_3_1
from student.models import mid2_3_1
from student.models import external_3_1
from student.models import counselling_3_1,problems_3_1,cstatus_3_1,student_profile
from student.models import *
from qr_profile.models import *
from .models import faprofile
from accounts.models import MyUser
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import pandas as pd
from django.apps import apps
import os
# Create your views here.

def hchange(request):
    if request.method=="POST":
        old=request.POST.get("old")
        new=request.POST.get("new")
        rnew=request.POST.get("rnew")
        a=MyUser.objects.get(username=request.user.username)
        if a.check_password(old):
            if new==rnew:
                a.set_password(new)
                a.save()
                messages.info(request,'password has been updated succefully!!!')
            else:
                messages.info(request,'please re-enter the password carefully!!!')
        else:
            messages.info(request,'please enter correct password!!!')
    return render(request,'counselling/hchange.html')

def counseling_students(request):
    if request.method=="POST":
        year=request.POST.get("year",False)
        semester=request.POST.get("sem",False)
        request.session['year'] = year
        request.session['semester'] = semester
        x='basic_'+year+'_'+semester
        model = apps.get_model('student', x)
        b=model.objects.filter(counsellor_name=request.user.username).order_by('uname')
        s=student_profile.objects.filter(year=year,sem=semester).order_by('uname')
        return render(request,'counselling/counseling_students.html',{'b':b,'s':s})
    else:
        s=student_profile.objects.all().order_by('uname')
        b=[]
        for i in s:
            year=i.year
            semester=i.sem
            x='basic_'+year+'_'+semester
            model = apps.get_model('student', x)
            c=model.objects.filter(counsellor_name=request.user.username,uname=i.uname)
            b.extend(c)
        return render(request,'counselling/counseling_students.html',{'b':b,'s':s})


def grant_access(request):
    s=student_profile.objects.all()
    b=[]
    for i in s:
        year=i.year
        semester=i.sem
        x='basic_'+year+'_'+semester
        model = apps.get_model('student', x)
        c=model.objects.filter(counsellor_name=request.user.username,uname=i.uname)
        b.extend(c)
    if request.method=="POST":
        for i in b:
            s=student_profile.objects.get(uname=i.uname)
            year=s.year
            semester=s.sem
            a='cstatus_'+year+'_'+semester
            model1 = apps.get_model('student', a)
            j=model1.objects.get(uname=i.uname)
            p=i.uname+'1'
            q=i.uname+'2'
            r=i.uname+'3'
            s=i.uname+'4'
            t=i.uname+'5'
            c1_status=request.POST.get(p)
            if(j.c1_status=="Completed"):
                c1_status="Completed"
            c2_status=request.POST.get(q)
            if(j.c2_status=="Completed"):
                c2_status="Completed"
            c3_status=request.POST.get(r) 
            if(j.c3_status=="Completed"):
                c3_status="Completed"
            c4_status=request.POST.get(s)
            if(j.c4_status=="Completed"):
                c4_status="Completed"
            c5_status=request.POST.get(t)
            if(j.c5_status=="Completed"):
                c5_status="Completed"
            b1=model1.objects.filter(uname=i.uname).exists()
            if(b1==False):
                b2=model1(uname=i.uname,counsellor_name=i.counsellor_name,c1_status=c1_status,c2_status=c2_status,c3_status=c3_status,c4_status=c4_status,c5_status=c5_status)
                b2.save()
            else:
                model1.objects.filter(uname=i.uname).update(counsellor_name=i.counsellor_name,c1_status=c1_status,c2_status=c2_status,c3_status=c3_status,c4_status=c4_status,c5_status=c5_status)
    s=student_profile.objects.all()
    b=[]
    b1=[]
    for i in s:
        year=i.year
        semester=i.sem
        x='basic_'+year+'_'+semester
        model = apps.get_model('student', x)
        c=model.objects.filter(counsellor_name=request.user.username,uname=i.uname)
        b.extend(c)
        a='cstatus_'+year+'_'+semester
        model1 = apps.get_model('student', a)
        b2=model1.objects.filter(counsellor_name=request.user.username,uname=i.uname)
        b1.extend(b2)
    return render(request,'counselling/grant_access.html',{'b':b,'b1':b1})

def fprofile(request):
    f=faprofile.objects.filter(uname=request.user.username).exists()
    pro2 = ProfFac.objects.get(email=request.user.username)
    if(f==False):
        f=faprofile(uname=request.user.username)
        f.save()
    if request.method=="POST":
        a=request.POST.get("faname")
        b=request.user.username
        c=request.POST.get("faph_no")
        dob = request.POST.get('dob')
        img = request.FILES.get('img')
        designation = request.POST.get('designation')
        address = request.POST.get('address')
        qualif = request.POST.get('qualif')
        tech_skl = request.POST.get('tech_skl')
        exp = request.POST.get('exp')
        subj = request.POST.get('subj')
        achv = request.POST.get('achv')
        res_area = request.POST.get('res_area')
        ref = request.POST.get('res_area')
        faprofile.objects.filter(uname=request.user.username).update(name=a,email=b,ph_no=c)
        if designation:
            ProfFac.objects.filter(email=request.user.username).update(desig=designation)
        if qualif:
            ProfFac.objects.filter(email=request.user.username).update(qualif=qualif)
        if a:
            ProfFac.objects.filter(email=request.user.username).update(name=a)
        if dob:
            ProfFac.objects.filter(email=request.user.username).update(dob=dob)
        if img:
            ProfFac.objects.filter(email=request.user.username).update(img=img)
        if c:
            ProfFac.objects.filter(email=request.user.username).update(phn=c)
        if address:
            ProfFac.objects.filter(email=request.user.username).update(address=address)
        if tech_skl:
            ProfFac.objects.filter(email=request.user.username).update(tech_skl=tech_skl)
        if exp:
            ProfFac.objects.filter(email=request.user.username).update(exp=exp)
        if subj:
            ProfFac.objects.filter(email=request.user.username).update(subj=subj)
        if achv:
            ProfFac.objects.filter(email=request.user.username).update(achv=achv)
        if res_area:
            ProfFac.objects.filter(email=request.user.username).update(res_area=res_area)
        if ref:
            ProfFac.objects.filter(email=request.user.username).update(ref=ref)
        #pro2.save()
    f=faprofile.objects.get(uname=request.user.username)
    return render(request,'counselling/fprofile.html',{"f":f,'pro2':pro2})

def view(request,x):
    s=student_profile.objects.get(uname=x)
    year=s.year
    semester=s.sem
    h='counselling_'+year+'_'+semester
    model = apps.get_model('student', h)
    b2=model.objects.filter(uname=x).exists()
    c='cstatus_'+year+'_'+semester
    model1= apps.get_model('student', c)
    j=model1.objects.get(uname=x)
    if(b2==False):
        b=model(uname=x)
        b.save()
    if request.method=="POST":
        c1_datetime=request.POST.get("dt1",False)
        c1_sugg=request.POST.get("sugg1",'')
        if(c1_sugg):
            model1.objects.filter(uname=x).update(c1_status='Completed')
        c1_eng=request.POST.get("e1",'')
        c1_mt=request.POST.get("m1",'')
        c1_conf=request.POST.get("c1",'')
        c1_knowledge=request.POST.get("k1",'')
        c1_health=request.POST.get("h1",'')
        c1_relation=request.POST.get("p1",'')
        c2_datetime=request.POST.get("dt2",False)
        c2_sugg=request.POST.get("sugg2",'')
        if(c2_sugg):
            model1.objects.filter(uname=x).update(c2_status='Completed')
        c2_eng=request.POST.get("e2",'')
        c2_mt=request.POST.get("m2",'')
        c2_conf=request.POST.get("c2",'')
        c2_knowledge=request.POST.get("k2",'')
        c2_health=request.POST.get("h2",'')
        c2_relation=request.POST.get("p2",'')
        c3_datetime=request.POST.get("dt3",False)
        c3_sugg=request.POST.get("sugg3",'')
        if(c3_sugg):
            model1.objects.filter(uname=x).update(c3_status='Completed')
        c3_eng=request.POST.get("e3",'')
        c3_mt=request.POST.get("m3",'')
        c3_conf=request.POST.get("c3",'')
        c3_knowledge=request.POST.get("k3",'')
        c3_health=request.POST.get("h3",'')
        c3_relation=request.POST.get("p3",'')
        c4_datetime=request.POST.get("dt4",False)
        c4_sugg=request.POST.get("sugg4",'')
        if(c4_sugg):
            model1.objects.filter(uname=x).update(c4_status='Completed')
        c4_eng=request.POST.get("e4",'')
        c4_mt=request.POST.get("m4",'')
        c4_conf=request.POST.get("c4",'')
        c4_knowledge=request.POST.get("k4",'')
        c4_health=request.POST.get("h4",'')
        c4_relation=request.POST.get("p4",'')
        c5_datetime=request.POST.get("dt5",False)
        c5_sugg=request.POST.get("sugg5",'')
        if(c5_sugg):
            model1.objects.filter(uname=x).update(c5_status='Completed')
        c5_eng=request.POST.get("e5",'')
        c5_mt=request.POST.get("m5",'')
        c5_conf=request.POST.get("c5",'')
        c5_knowledge=request.POST.get("k5",'')
        c5_health=request.POST.get("h5",'')
        c5_relation=request.POST.get("p5",'')
        b2=model.objects.filter(uname=x).exists()
        if(b2==False):
            b=model(uname=x,c1_datetime=c1_datetime,c1_sugg=c1_sugg,c1_eng=c1_eng,c1_mt=c1_mt,c1_conf=c1_conf,c1_knowledge=c1_knowledge,c1_health=c1_health,c1_relation=c1_relation,c2_datetime=c2_datetime,c2_sugg=c2_sugg,c2_eng=c2_eng,c2_mt=c2_mt,c2_conf=c2_conf,c2_knowledge=c2_knowledge,c2_health=c2_health,c2_relation=c2_relation,c3_datetime=c3_datetime,c3_sugg=c3_sugg,c3_eng=c3_eng,c3_mt=c3_mt,c3_conf=c3_conf,c3_knowledge=c3_knowledge,c3_health=c3_health,c3_relation=c3_relation,c4_datetime=c4_datetime,c4_sugg=c4_sugg,c4_eng=c4_eng,c4_mt=c4_mt,c4_conf=c4_conf,c4_knowledge=c4_knowledge,c4_health=c4_health,c4_relation=c4_relation,c5_datetime=c5_datetime,c5_sugg=c5_sugg,c5_eng=c5_eng,c5_mt=c5_mt,c5_conf=c5_conf,c5_knowledge=c5_knowledge,c5_health=c5_health,c5_relation=c5_relation)
            b.save()
        else:
            b3=model.objects.get(uname=x)
            c1_datetime=request.POST.get("dt1",b3.c1_datetime)
            c1_sugg=request.POST.get("sugg1",b3.c1_sugg)
            c1_eng=request.POST.get("e1",b3.c1_eng)
            c1_mt=request.POST.get("m1",b3.c1_mt)
            c1_conf=request.POST.get("c1",b3.c1_conf)
            c1_knowledge=request.POST.get("k1",b3.c1_knowledge)
            c1_health=request.POST.get("h1",b3.c1_health)
            c1_relation=request.POST.get("p1",b3.c1_relation)
            c2_datetime=request.POST.get("dt2",b3.c2_datetime)
            c2_sugg=request.POST.get("sugg2",b3.c2_sugg)
            c2_eng=request.POST.get("e2",b3.c2_eng)
            c2_mt=request.POST.get("m2",b3.c2_mt)
            c2_conf=request.POST.get("c2",b3.c2_conf)
            c2_knowledge=request.POST.get("k2",b3.c2_knowledge)
            c2_health=request.POST.get("h2",b3.c2_health)
            c2_relation=request.POST.get("p2",b3.c2_relation)
            c3_datetime=request.POST.get("dt3",b3.c3_datetime)
            c3_sugg=request.POST.get("sugg3",b3.c3_sugg)
            c3_eng=request.POST.get("e3",b3.c3_eng)
            c3_mt=request.POST.get("m3",b3.c3_mt)
            c3_conf=request.POST.get("c3",b3.c3_conf)
            c3_knowledge=request.POST.get("k3",b3.c3_knowledge)
            c3_health=request.POST.get("h3",b3.c3_health)
            c3_relation=request.POST.get("p3",b3.c3_relation)
            c4_datetime=request.POST.get("dt4",b3.c4_datetime)
            c4_sugg=request.POST.get("sugg4",b3.c4_sugg)
            c4_eng=request.POST.get("e4",b3.c4_eng)
            c4_mt=request.POST.get("m4",b3.c4_mt)
            c4_conf=request.POST.get("c4",b3.c4_conf)
            c4_knowledge=request.POST.get("k4",b3.c4_knowledge)
            c4_health=request.POST.get("h4",b3.c4_health)
            c4_relation=request.POST.get("p4",b3.c4_relation)
            c5_datetime=request.POST.get("dt5",b3.c5_datetime)
            c5_sugg=request.POST.get("sugg5",b3.c5_sugg)
            c5_eng=request.POST.get("e5",b3.c5_eng)
            c5_mt=request.POST.get("m5",b3.c5_mt)
            c5_conf=request.POST.get("c5",b3.c5_conf)
            c5_knowledge=request.POST.get("k5",b3.c5_knowledge)
            c5_health=request.POST.get("h5",b3.c5_health)
            c5_relation=request.POST.get("p5",b3.c5_relation)
            model.objects.filter(uname=x).update(c1_datetime=c1_datetime,c1_sugg=c1_sugg,c1_eng=c1_eng,c1_mt=c1_mt,c1_conf=c1_conf,c1_knowledge=c1_knowledge,c1_health=c1_health,c1_relation=c1_relation,c2_datetime=c2_datetime,c2_sugg=c2_sugg,c2_eng=c2_eng,c2_mt=c2_mt,c2_conf=c2_conf,c2_knowledge=c2_knowledge,c2_health=c2_health,c2_relation=c2_relation,c3_datetime=c3_datetime,c3_sugg=c3_sugg,c3_eng=c3_eng,c3_mt=c3_mt,c3_conf=c3_conf,c3_knowledge=c3_knowledge,c3_health=c3_health,c3_relation=c3_relation,c4_datetime=c4_datetime,c4_sugg=c4_sugg,c4_eng=c4_eng,c4_mt=c4_mt,c4_conf=c4_conf,c4_knowledge=c4_knowledge,c4_health=c4_health,c4_relation=c4_relation,c5_datetime=c5_datetime,c5_sugg=c5_sugg,c5_eng=c5_eng,c5_mt=c5_mt,c5_conf=c5_conf,c5_knowledge=c5_knowledge,c5_health=c5_health,c5_relation=c5_relation) 
    p=student_profile.objects.get(uname=x)
    b111=basic_1_1.objects.get(uname=x)
    b211=mid1_1_1.objects.get(uname=x)
    b311=mid2_1_1.objects.get(uname=x)
    b411=external_1_1.objects.get(uname=x)
    b511=counselling_1_1.objects.get(uname=x)
    b611=problems_1_1.objects.get(uname=x)
    b112=basic_1_2.objects.get(uname=x)
    b212=mid1_1_2.objects.get(uname=x)
    b312=mid2_1_2.objects.get(uname=x)
    b412=external_1_2.objects.get(uname=x)
    b512=counselling_1_2.objects.get(uname=x)
    b612=problems_1_2.objects.get(uname=x)
    b121=basic_2_1.objects.get(uname=x)
    b221=mid1_2_1.objects.get(uname=x)
    b321=mid2_2_1.objects.get(uname=x)
    b421=external_2_1.objects.get(uname=x)
    b521=counselling_2_1.objects.get(uname=x)
    b621=problems_2_1.objects.get(uname=x)
    b122=basic_2_2.objects.get(uname=x)
    b222=mid1_2_2.objects.get(uname=x)
    b322=mid2_2_2.objects.get(uname=x)
    b422=external_2_2.objects.get(uname=x)
    b522=counselling_2_2.objects.get(uname=x)
    b622=problems_2_2.objects.get(uname=x)
    b131=basic_3_1.objects.get(uname=x)
    b231=mid1_3_1.objects.get(uname=x)
    b331=mid2_3_1.objects.get(uname=x)
    b431=external_3_1.objects.get(uname=x)
    b531=counselling_3_1.objects.get(uname=x)
    b631=problems_3_1.objects.get(uname=x)
    b132=basic_3_2.objects.get(uname=x)
    b232=mid1_3_2.objects.get(uname=x)
    b332=mid2_3_2.objects.get(uname=x)
    b432=external_3_2.objects.get(uname=x)
    b532=counselling_3_2.objects.get(uname=x)
    b632=problems_3_2.objects.get(uname=x)
    b141=basic_4_1.objects.get(uname=x)
    b241=mid1_4_1.objects.get(uname=x)
    b341=mid2_4_1.objects.get(uname=x)
    b441=external_4_1.objects.get(uname=x)
    b541=counselling_4_1.objects.get(uname=x)
    b641=problems_4_1.objects.get(uname=x)
    b142=basic_4_2.objects.get(uname=x)
    b242=mid1_4_2.objects.get(uname=x)
    b342=mid2_4_2.objects.get(uname=x)
    b442=external_4_2.objects.get(uname=x)
    b542=counselling_4_2.objects.get(uname=x)
    b642=problems_4_2.objects.get(uname=x)
    p=student_profile.objects.get(uname=x)
    a=MyUser.objects.get(username=j.counsellor_name)
    return render(request,'counselling/view.html',{"a":a,"p":p,"b111":b111,"b211":b211,"b311":b311,'b411':b411,"b112":b112,"b212":b212,"b312":b312,'b412':b412,"b121":b121,"b221":b221,"b321":b321,'b421':b421,"b122":b122,"b222":b222,"b322":b322,'b422':b422,"b121":b131,"b231":b231,"b331":b331,'b431':b431,"b132":b132,"b232":b232,"b332":b332,'b432':b432,"b141":b141,"b241":b241,"b341":b341,'b441':b441,"b142":b142,"b242":b242,"b342":b342,'b442':b442,'b641':b641,'b541':b541,'b642':b642,'b542':b542,'b631':b631,'b531':b531,'b632':b632,'b532':b532,'b621':b621,'b521':b521,'b622':b622,'b522':b522,'b611':b611,'b511':b511,'b612':b612,'b512':b512})


from pathlib import Path

def add_counsellor(request):            
    try:
        if request.method == 'POST' and request.FILES['myfile'] :     
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
                b=basic_2_1.objects.filter(uname=dbframe.rollno).exists()
                if (b==False):
                    b=basic_2_1(uname=dbframe.rollno,counsellor_name=dbframe.cname,present_cname=dbframe.cname,roll_no=dbframe.rollno,year=2,semester=1)
                    b.save()
                basic_2_1.objects.filter(uname=dbframe.rollno).update(counsellor_name=dbframe.cname,present_cname=dbframe.cname,roll_no=dbframe.rollno,year=2,semester=1)
                b=basic_2_2.objects.filter(uname=dbframe.rollno).exists()
                if (b==False):
                    b=basic_2_2(uname=dbframe.rollno,counsellor_name=dbframe.cname,present_cname=dbframe.cname,roll_no=dbframe.rollno,year=2,semester=2)
                    b.save()
                basic_2_2.objects.filter(uname=dbframe.rollno).update(counsellor_name=dbframe.cname,present_cname=dbframe.cname,roll_no=dbframe.rollno,year=2,semester=2)
                b=basic_3_1.objects.filter(uname=dbframe.rollno).exists()
                if (b==False):
                    b=basic_3_1(uname=dbframe.rollno,counsellor_name=dbframe.cname,present_cname=dbframe.cname,roll_no=dbframe.rollno,year=3,semester=1)
                    b.save()
                basic_3_1.objects.filter(uname=dbframe.rollno).update(counsellor_name=dbframe.cname,present_cname=dbframe.cname,roll_no=dbframe.rollno,year=3,semester=1)
                b=basic_3_2.objects.filter(uname=dbframe.rollno).exists()
                if (b==False):
                    b=basic_3_2(uname=dbframe.rollno,counsellor_name=dbframe.cname,present_cname=dbframe.cname,roll_no=dbframe.rollno,year=3,semester=2)
                    b.save()
                basic_3_2.objects.filter(uname=dbframe.rollno).update(counsellor_name=dbframe.cname,present_cname=dbframe.cname,roll_no=dbframe.rollno,year=3,semester=2)
                b=basic_4_1.objects.filter(uname=dbframe.rollno).exists()
                if (b==False):
                    b=basic_4_1(uname=dbframe.rollno,counsellor_name=dbframe.cname,present_cname=dbframe.cname,roll_no=dbframe.rollno,year=4,semester=1)
                    b.save()
                basic_4_1.objects.filter(uname=dbframe.rollno).update(counsellor_name=dbframe.cname,present_cname=dbframe.cname,roll_no=dbframe.rollno,year=4,semester=1)
                b=basic_4_2.objects.filter(uname=dbframe.rollno).exists()
                if (b==False):
                    b=basic_4_2(uname=dbframe.rollno,counsellor_name=dbframe.cname,present_cname=dbframe.cname,roll_no=dbframe.rollno,year=4,semester=2)
                    b.save()
                basic_4_2.objects.filter(uname=dbframe.rollno).update(counsellor_name=dbframe.cname,present_cname=dbframe.cname,roll_no=dbframe.rollno,year=4,semester=2)
                b=cstatus_2_1.objects.filter(uname=dbframe.rollno).exists()
                if (b==False):
                    b=cstatus_2_1(uname=dbframe.rollno,counsellor_name=dbframe.cname,roll_no=dbframe.rollno)
                    b.save()
                cstatus_2_1.objects.filter(uname=dbframe.rollno).update(counsellor_name=dbframe.cname,roll_no=dbframe.rollno)
                b=cstatus_2_2.objects.filter(uname=dbframe.rollno).exists()
                if (b==False):
                    b=cstatus_2_2(uname=dbframe.rollno,counsellor_name=dbframe.cname,roll_no=dbframe.rollno)
                    b.save()
                cstatus_2_2.objects.filter(uname=dbframe.rollno).update(counsellor_name=dbframe.cname,roll_no=dbframe.rollno)
                b=cstatus_3_1.objects.filter(uname=dbframe.rollno).exists()
                if (b==False):
                    b=cstatus_3_1(uname=dbframe.rollno,counsellor_name=dbframe.cname,roll_no=dbframe.rollno)
                    b.save()
                cstatus_3_1.objects.filter(uname=dbframe.rollno).update(counsellor_name=dbframe.cname,roll_no=dbframe.rollno)
                b=cstatus_3_2.objects.filter(uname=dbframe.rollno).exists()
                if (b==False):
                    b=cstatus_3_2(uname=dbframe.rollno,counsellor_name=dbframe.cname,roll_no=dbframe.rollno)
                    b.save()
                cstatus_3_2.objects.filter(uname=dbframe.rollno).update(counsellor_name=dbframe.cname,roll_no=dbframe.rollno)
                b=cstatus_4_1.objects.filter(uname=dbframe.rollno).exists()
                if (b==False):
                    b=cstatus_4_1(uname=dbframe.rollno,counsellor_name=dbframe.cname,roll_no=dbframe.rollno)
                    b.save()
                cstatus_4_1.objects.filter(uname=dbframe.rollno).update(counsellor_name=dbframe.cname,roll_no=dbframe.rollno)
                b=cstatus_4_2.objects.filter(uname=dbframe.rollno).exists()
                if (b==False):
                    b=cstatus_4_2(uname=dbframe.rollno,counsellor_name=dbframe.cname,roll_no=dbframe.rollno)
                    b.save()
                cstatus_4_2.objects.filter(uname=dbframe.rollno).update(counsellor_name=dbframe.cname,roll_no=dbframe.rollno)
            return render(request, 'counselling/add_counsellor.html', {
                'uploaded_file_url': uploaded_file_url}) 
    except Exception as identifier:            
        print(identifier)
     
    return render(request, 'counselling/add_counsellor.html',{})

def update_sem(request):
    try:
        if  request.method == 'POST' or  request.FILES['myfile']:
            y=request.POST.get('year')
            s=request.POST.get('sem')
            if y=='none' and s=='none':
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
                    k=student_profile.objects.filter(uname=dbframe.username).exists()
                    if k==False:
                        student_profile(uname=dbframe.username,year=dbframe.year,sem=dbframe.sem,done='0').save()
                    student_profile.objects.filter(uname=dbframe.username).update(year=dbframe.year,sem=dbframe.sem)
            else:
                if y=='1':
                    if s=='1':
                        student_profile.objects.filter(year=y,sem=s).update(year='1',sem='2')
                    else:
                        student_profile.objects.filter(year=y,sem=s).update(year='2',sem='1')
                if y=='2':
                    if s=='1':
                        student_profile.objects.filter(year=y,sem=s).update(year='2',sem='2')
                    else:
                        student_profile.objects.filter(year=y,sem=s).update(year='3',sem='1')
                if y=='3':
                    if s=='1':
                        student_profile.objects.filter(year='3',sem='1').update(year='3',sem='2')
                    else:
                        student_profile.objects.filter(year=y,sem=s).update(year='4',sem='1')
                if y=='4':
                    if s=='1':
                        student_profile.objects.filter(year=y,sem=s).update(year='4',sem='2')
    except Exception as identifier:            
        pass
    return render(request,'counselling/update_sem.html')

def admin_home(request):
    return render(request,'counselling/admin_home.html')

def view_form(request):
    if request.method=="POST":
        year=request.POST.get("year",False)
        semester=request.POST.get("sem",False)
        request.session['year'] = year
        request.session['semester'] = semester
        s=student_profile.objects.filter(year=year,sem=semester)
        return render(request,'counselling/view_form.html',{'s':s})
    else:
        s=student_profile.objects.all().order_by('uname')
        return render(request,'counselling/view_form.html',{'s':s})

def show(request,x):
    p=student_profile.objects.get(uname=x)
    b111=basic_1_1.objects.get(uname=x)
    b211=mid1_1_1.objects.get(uname=x)
    b311=mid2_1_1.objects.get(uname=x)
    b411=external_1_1.objects.get(uname=x)
    b511=counselling_1_1.objects.get(uname=x)
    b611=problems_1_1.objects.get(uname=x)
    b112=basic_1_2.objects.get(uname=x)
    b212=mid1_1_2.objects.get(uname=x)
    b312=mid2_1_2.objects.get(uname=x)
    b412=external_1_2.objects.get(uname=x)
    b512=counselling_1_2.objects.get(uname=x)
    b612=problems_1_2.objects.get(uname=x)
    b121=basic_2_1.objects.get(uname=x)
    b221=mid1_2_1.objects.get(uname=x)
    b321=mid2_2_1.objects.get(uname=x)
    b421=external_2_1.objects.get(uname=x)
    b521=counselling_2_1.objects.get(uname=x)
    b621=problems_2_1.objects.get(uname=x)
    b122=basic_2_2.objects.get(uname=x)
    b222=mid1_2_2.objects.get(uname=x)
    b322=mid2_2_2.objects.get(uname=x)
    b422=external_2_2.objects.get(uname=x)
    b522=counselling_2_2.objects.get(uname=x)
    b622=problems_2_2.objects.get(uname=x)
    b131=basic_3_1.objects.get(uname=x)
    b231=mid1_3_1.objects.get(uname=x)
    b331=mid2_3_1.objects.get(uname=x)
    b431=external_3_1.objects.get(uname=x)
    b531=counselling_3_1.objects.get(uname=x)
    b631=problems_3_1.objects.get(uname=x)
    b132=basic_3_2.objects.get(uname=x)
    b232=mid1_3_2.objects.get(uname=x)
    b332=mid2_3_2.objects.get(uname=x)
    b432=external_3_2.objects.get(uname=x)
    b532=counselling_3_2.objects.get(uname=x)
    b632=problems_3_2.objects.get(uname=x)
    b141=basic_4_1.objects.get(uname=x)
    b241=mid1_4_1.objects.get(uname=x)
    b341=mid2_4_1.objects.get(uname=x)
    b441=external_4_1.objects.get(uname=x)
    b541=counselling_4_1.objects.get(uname=x)
    b641=problems_4_1.objects.get(uname=x)
    b142=basic_4_2.objects.get(uname=x)
    b242=mid1_4_2.objects.get(uname=x)
    b342=mid2_4_2.objects.get(uname=x)
    b442=external_4_2.objects.get(uname=x)
    b542=counselling_4_2.objects.get(uname=x)
    b642=problems_4_2.objects.get(uname=x)
    s=student_profile.objects.get(uname=x)
    b='basic_'+s.year+'_'+s.sem
    model1= apps.get_model('student', b)
    j=model1.objects.get(uname=x)
    s=MyUser.objects.get(username=j.counsellor_name)
    sample={"s":s,"b111":b111,"b211":b211,"b311":b311,'b411':b411,'b511':b511,'b611':b611,"b112":b112,"b212":b212,"b312":b312,'b412':b412,'b512':b512,'b612':b612,
            "b121":b121,"b221":b221,"b321":b321,'b421':b421,'b521':b521,'b621':b621,"b122":b122,"b222":b222,"b322":b322,'b422':b422,'b522':b522,'b622':b622,
            "b121":b131,"b231":b231,"b331":b331,'b431':b431,'b531':b531,'b631':b631,"b132":b132,"b232":b232,"b332":b332,'b432':b432,'b532':b532,'b632':b632,
            "b141":b141,"b241":b241,"b341":b341,'b441':b441,'b541':b541,'b641':b641,"b142":b142,"b242":b242,"b342":b342,'b442':b442,'b542':b542,'b642':b642,'p':p}
    return render(request,'counselling/show.html',sample)

def status(request):
    s=student_profile.objects.all()
    '''b=[]
    for i in s:
        year=i.year
        semester=i.sem
        x='basic_'+year+'_'+semester
        model = apps.get_model('student', x)
        c=model.objects.filter(counsellor_name=request.user.username,uname=i.uname)
        b.extend(c)
    if request.method=="POST":'''
    for i in s:
        year=i.year
        semester=i.sem
        a='cstatus_'+year+'_'+semester
        model1 = apps.get_model('student', a)
        j=model1.objects.get(uname=i.uname)
        p=i.uname+'1'
        q=i.uname+'2'
        r=i.uname+'3'
        s=i.uname+'4'
        t=i.uname+'5'
        c1_status=request.POST.get(p)
        if(j.c1_status=="Completed"):
            c1_status="Completed"
        c2_status=request.POST.get(q)
        if(j.c2_status=="Completed"):
            c2_status="Completed"
        c3_status=request.POST.get(r) 
        if(j.c3_status=="Completed"):
            c3_status="Completed"
        c4_status=request.POST.get(s)
        if(j.c4_status=="Completed"):
            c4_status="Completed"
        c5_status=request.POST.get(t)
        if(j.c5_status=="Completed"):
            c5_status="Completed"
        b1=model1.objects.filter(uname=i.uname).exists()
        if(b1==False):
            b2=model1(uname=i.uname,c1_status=c1_status,c2_status=c2_status,c3_status=c3_status,c4_status=c4_status,c5_status=c5_status)
            b2.save()
        else:
            model1.objects.filter(uname=i.uname).update(c1_status=c1_status,c2_status=c2_status,c3_status=c3_status,c4_status=c4_status,c5_status=c5_status)
    s=student_profile.objects.all()
    b=[]
    b1=[]
    for i in s:
        year=i.year
        semester=i.sem
        x='basic_'+year+'_'+semester
        model = apps.get_model('student', x)
        c=model.objects.filter(uname=i.uname)
        b.extend(c)
        a='cstatus_'+year+'_'+semester
        model1 = apps.get_model('student', a)
        b2=model1.objects.filter(uname=i.uname)
        b1.extend(b2)
    return render(request,'counselling/status.html',{'b':b,'b1':b1})