from django.db import models

# Create your models here.
class Placement(models.Model):
    url = models.URLField()
    year = models.CharField(max_length=30,default="")

    def __str__(self):
        return self.year

class News(models.Model):
    title=models.CharField(max_length=200,default="")
    url=models.URLField()
    date = models.DateField()

    def __str__(self):
        return self.title

class Fac(models.Model):
    pic = models.ImageField()
    name = models.CharField(max_length=200,default="")
    designation = models.CharField(max_length=100,default="")
    email=models.EmailField()
    qualif = models.CharField(max_length=100,default="")
    resume = models.FileField()

    def __str__(self):
        return self.name

class acheivement(models.Model):
    pic = models.ImageField()
    name = models.CharField(max_length=200,default="")
    achieve = models.CharField(max_length=1000,default="")

    def __str__(self):
        return self.name

class Contact(models.Model):
    fname=models.CharField(max_length=200,default="")
    lname=models.CharField(max_length=200,default="")
    email=models.EmailField()
    subject=models.CharField(max_length=200,default="")
    msg=models.CharField(max_length=200,default="")

    def __str__(self):
        return self.fname