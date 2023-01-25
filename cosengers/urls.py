from django.urls import path

from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('del_event/<int:pk>/',views.del_event,name="del_event"),
    path('<int:pk>/',views.event,name="event"),
    path('add/',views.add),
    path('add_event/',views.add_event,name="add_event"),
    path('about/',views.about,name="about"),
    path('reg_evn/',views.reg_evn,name="reg_evn"),
    path('add_blog/',views.add_blog,name="add_blog"),
    path('del_blog/<int:pk>/',views.del_blog,name="del_blog"),
    path('blogs/',views.blogs,name="blogs"),
    path('del_ev_det/<int:pk>',views.del_ev_det,name="del_ev_det"),
]
