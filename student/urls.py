from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('form',views.form,name="form"),
    path('fill',views.fill,name="fill"),
    path('fill2',views.fill2,name="fill2"),
    path('profile',views.profile,name="profile"),
    path('basic_details',views.basic_details,name="basic_details"),
    path('mid1',views.mid1,name="mid1"),
    path('mid2',views.mid2,name="mid2"),
    path('external',views.external,name="external"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('counseling',views.counseling,name="counseling"),
    path('change',views.change,name="change"),
]