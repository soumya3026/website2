from django.db import models

# Create your models here.
class Table(models.Model):
    EventMode = models.CharField(max_length=40,blank=True)
    EventType = models.CharField(max_length=100,blank=True)
    UploadLink = models.URLField(max_length=500,unique=True)
    EventDate = models.DateField(blank=True,null=True,auto_now=False,auto_now_add=False)
    Location = models.CharField(max_length=80,blank=True)
    Month    =models.CharField(max_length=20,blank=True)
    def __str__(self):
      return self.UploadLink

class Event(models.Model):
  name = models.CharField(max_length=100,default="")
  date = models.DateField()
  activity = models.CharField(max_length=150,default="")
  res_persn = models.CharField(max_length=150,default="")
  remarks = models.CharField(max_length=200,default="")
  relevance = models.CharField(max_length=100,default="")
  img1 = models.ImageField(default="")
  img2 = models.ImageField(default="")
  img3 = models.ImageField(default="")

  def __str__(self):
    return self.name


class NewEvent(models.Model):
  name = models.CharField(max_length=150,default="")
  date = models.DateTimeField(default="")
  link = models.URLField(default="")
  desc = models.CharField(max_length=300,default="")

  def __str__(self):
    return self.name

class NewBlog(models.Model):
  title = models.CharField(max_length=100,default="")
  desc = models.CharField(max_length=500,default="")
  img = models.ImageField(default="")

  def __str__(self):
    return self.title
