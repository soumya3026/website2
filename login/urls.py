from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('signin/',views.signin,name='signin'),
    path('logout/',views.logout,name="logout"),
]