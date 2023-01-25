from django.db import models
from django.db.models.deletion import CASCADE
from cloudinary.models import CloudinaryField

# Create your models here.

class Detail(models.Model):
    use  = models.CharField(max_length=200,default=" ")
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    qualif = models.CharField(max_length=200)

    def __str__(self):
        return str(self.use)


class Exam(models.Model):
    exm = models.CharField(max_length=200,default="")

    def __str__(self):
        return self.exm


class Degree(models.Model):
    #degr = models.ForeignKey(Degree,on_delete=models.CASCADE,default="general",related_name="display")
    deg = models.CharField(max_length=200,default="")
    exm = models.ManyToManyField(Exam)

    def __str__(self):
        return self.deg

class Appeared(models.Model):
    nam = models.CharField(max_length=200)
    enam = models.CharField(max_length=200)

    def __str__(self):
        return self.nam



class Photo(models.Model):
    # title field
    use = models.CharField(max_length=200,default=" ")
    title = models.CharField(max_length=100)
    #image field
    image = models.FileField(default='')
    #image = CloudinaryField('image')


class ProfFac(models.Model):
    name = models.CharField(max_length=50,default="")
    dob = models.DateField(default="")
    email = models.EmailField(default="")
    img = models.FileField(default="")
    desig = models.CharField(max_length=100,default="")
    phn = models.CharField(max_length=20,default="")
    address = models.CharField(max_length=200,default="")
    qualif = models.CharField(max_length=500,default="")
    tech_skl = models.CharField(max_length=200,default="")
    exp = models.TextField(default="")
    subj = models.CharField(max_length=200,default="")
    achv = models.TextField(default="")
    res_area = models.CharField(max_length=500,default="")
    ref = models.TextField(default="")

    def __str__(self):
        return self.name

