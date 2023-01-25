from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('counseling_students',views.counseling_students,name="counseling_students"),
    path('view_form',views.view_form,name='view_form'),
    path('add_counsellor',views.add_counsellor,name="add_counsellor"),
    path('admin_home',views.admin_home,name="admin_home"),
    path('update_sem',views.update_sem,name='update_sem'),
    path('grant_access',views.grant_access,name="grant_access"),
    path(r'view-(?P<x>[\w-]+)',views.view,name="view"),
    path(r'show-(?P<x>[\w-]+)',views.show,name="show"),
    path('status',views.status,name="status"),
    path('fprofile',views.fprofile,name="fprofile"),
    path('hchange',views.hchange,name="hchange"),
]