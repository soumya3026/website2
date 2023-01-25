from django.urls import path
##from django.contrib import admin
from . import views
app_name='qr_profile'
urlpatterns = [
    #path('',views.index,name="index"),
    path('',views.detail,name="detail"),
    path('upload/',views.upload,name="upload"),
   
    path('select/',views.select,name='select'),
    path('quick/',views.quick,name="quick"),
    path('gen/',views.gen,name="gen"),
    path('delete/',views.delete,name="delete"),
    path('upd/',views.upd,name="upd"),
    path('resum/<int:pk>/',views.resum,name="resum"),
    path('disp/<int:pk>/',views.disp,name="disp"),
    path('del_doc/<int:pk>',views.del_doc,name="del_doc"),
]
