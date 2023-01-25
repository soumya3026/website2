from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import MyUser

# Register your models here.

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    list_display = ['username','email','first_name','last_name','is_staff','is_student','is_faculty','password']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('is_student','is_faculty')}),
    ) 


admin.site.register(MyUser, MyUserAdmin)
