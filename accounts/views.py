from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import MyUser
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings 
from django.core.mail import send_mail,get_connection
from django.template.loader import render_to_string
from student.models import student_profile

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            if(request.user.is_student):
                return render(request,'counselling/fill.html')
            if(request.user.is_faculty):
                return render(request,'counselling/counseling_students.html')
            #return redirect('/')
            return render(request,'counselling/fill.html')
        else:
            messages.info(request,' invalid login, please try again. ')
            return redirect('/')
    else:
        return render(request,'counselling/login.html')

def forgot(request):
        global em1
        if request.method=='POST':
                em1 = request.POST.get("email")
                print(em1)
                a=MyUser.objects.filter(email=em1).exists()
                b=MyUser.objects.get(email=em1)
                if a==True:
                    subject = 'Reset Password'
                    #file = open(MEDIA_ROOT + os.path.sep + 'files/reset.txt', 'r')
                    #content = file.read()
                    #file.close()
                   
                    k={
                        "email":em1,
                        'domain':'127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(b.id)),
                        "user": b,
                        'token': default_token_generator.make_token(b),
                        'protocol': 'http',
                    }
                    email1=render_to_string("reset.txt",k)
                    send_mail(subject, email1, settings.EMAIL_HOST_USER, [em1])
                    messages.info(request,'Instructions have been sent to your mail')
                return render(request,'counselling/login.html')
        return render(request,'counselling/forgot.html')

def reset(request, *args, **kwargs):
        return render(request,'counselling/reset.html')

def reset1(request):
        a=MyUser.objects.get(email=em1)
        if request.method=='POST':
                password=request.POST.get("password")
                password1=request.POST.get("password1")
                if password==password1:
                    a.set_password(password)
                    a.save()
                    messages.info(request,'password has been updated succefully!!!')
                else:
                    messages.info(request,'password doesn\'t match')
                    return render(request,'counselling/reset.html')
        return render(request,'counselling/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
    
