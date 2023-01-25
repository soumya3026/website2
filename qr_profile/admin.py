from django.contrib import admin
from .models import Detail, Exam, Degree, Appeared, Photo, ProfFac
# Register your models here.


admin.site.register(Detail)
admin.site.register(Degree)
admin.site.register(Exam)
admin.site.register(Appeared)
admin.site.register(Photo)
admin.site.register(ProfFac)