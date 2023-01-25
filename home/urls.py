from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.index,name='index'),
    path('dept_abt/',views.dept_abt,name='dept_abt'),
    path('faculty/',views.faculty,name='faculty'),
    path('contact/',views.contact,name="contact"),
    path('placements/',views.placements,name="placements"),
    path('add_placement/',views.add_placement,name="add_placement"),
    path('add_news/',views.add_news,name="add_news"),
    path('add_faculty/',views.add_faculty,name="add_faculty"),
    path('add_achievement/',views.add_achievement,name="add_achievement"),
    path('adminst/',views.adminst,name="adminst"),
    path('add_student/',views.add_student,name="add_student"),
    path('delete_fac/<int:pk>/',views.delete_fac,name="delete_fac"),
    path('team/',views.team,name="team"),
    path('resum/<int:pk>/',views.resum,name="resum"),
]