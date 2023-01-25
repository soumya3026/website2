from collections import namedtuple
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('about_us/',views.about_us,name="about_us"),
    path('blogs/',views.blogs,name="blogs"),
    path('index/',views.index,name="index"),
    path('events/',views.events,name="events"),
    path('upload_events/',views.upload_events,name="upload_events"),
    path('delete_blogs/<int:pk>/',views.delete_blogs,name="delete_blogs"),
    path('delete_events/<int:pk>/',views.delete_events,name="delete_events"),
    path('upload_blogs/',views.upload_blogs,name="upload_blogs"),
    path('add_evn/',views.add_evn,name="add_evn"),
    path('abt_evn/<int:pk>',views.abt_evn,name="abt_evn"),
    path('del_eve/<int:pk>',views.del_eve,name="del_eve"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


