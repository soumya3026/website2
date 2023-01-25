from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.login,name="login"),
    path('student/',include('student.urls')),
    path('faculty/',include('faculty.urls')),
    path('forgot',views.forgot,name="forgot"),
    path('reset/<uidb64>/<token>/',views.reset,name='password_reset_confirm'),
    path('reset1',views.reset1,name="reset1"),
    path('logout',views.logout,name="logout")
]