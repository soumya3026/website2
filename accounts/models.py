from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    is_student = models.BooleanField('student status', default=False)
    is_faculty = models.BooleanField('faculty status', default=False)
