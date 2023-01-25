from django import forms
from django import forms


from .models import nevents,blog


class XYZ_DateInput(forms.DateInput):
    input_type = "date"
    def __init__(self, **kwargs):
        #kwargs["format"] = "%Y-%m-%d"
        kwargs["format"] = "%d-%m-%Y"
        super().__init__(**kwargs)

class neventsForm(forms.ModelForm):
    class Meta:
        model = nevents
        fields=('title','desc','img','link','date')
        widgets = {
            'date':XYZ_DateInput(format=["%d-%m-%Y"],),
        }


class nblogsForm(forms.ModelForm):
    class Meta:
        model = blog
        fields=('title','desc','date','img')
        widgets = {
            'date':XYZ_DateInput(format=["%d-%m-%Y"],),
        }


