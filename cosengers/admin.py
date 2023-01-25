from django.contrib import admin
from .models import NewBlog, NewEvent, Table,Event

# Register your models here.
admin.site.register(Table)
admin.site.register(Event)
admin.site.register(NewEvent)
admin.site.register(NewBlog)
