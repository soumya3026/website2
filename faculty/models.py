from django.db import models

# Create your models here.
class faprofile(models.Model):
    uname=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    ph_no=models.CharField(max_length=10)

    def __str__(self):
        return self.name