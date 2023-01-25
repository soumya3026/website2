from distutils.command.upload import upload
from django.db import models

# Create your models here.
class face(models.Model):
    name = models.CharField(max_length=200,default='')
    is_cosenger = models.BooleanField(default=False)
    is_picsl = models.BooleanField(default=False)

    def __str__(self):
        return self.name

