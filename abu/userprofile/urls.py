from django.urls import path,include
from . import views

app_name='userprofile'

urlpatterns=[
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
]
