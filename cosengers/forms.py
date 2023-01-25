from django import forms
from django.forms import ModelForm
from .models import *

class DestinationForm(ModelForm):
    class Meta:
        model = Table
        fields = ['EventMode','EventType','UploadLink','Location','EventDate','Month']