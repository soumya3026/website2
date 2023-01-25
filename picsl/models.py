from django.core.exceptions import MultipleObjectsReturned
from django.core.files.storage import FileSystemStorage, default_storage
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from accounts.models import MyUser
from django.urls import reverse
import datetime
# Create your models here.


    

def get_upload_path(instance,org_name):
    return '{0}'.format(org_name)


class nevents(models.Model): 
    
    title=models.CharField(max_length=300)
    desc=models.TextField(max_length=4000)
    img=models.ImageField()
    date=models.DateField()
    link = models.URLField(max_length=500,unique=True)


    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

class blog(models.Model): 
    title=models.TextField(max_length=300)
    desc=models.TextField(max_length=4000)
    date=models.DateField()
    img=models.ImageField()



class eventdetails(models.Model):
    title = models.CharField(max_length=150,default="")
    fromdate = models.DateField(blank=True, null=True)
    todate = models.DateField(blank=True, null=True)
    desc = models.CharField(max_length=300,default="")
    img1=models.ImageField()
    img2=models.ImageField()
    img3=models.ImageField()

    def __str__(self):
        return self.title
