from django.urls import path
from . import views

app_name='whitelist'
urlpatterns = [
    path('addip/',views.addip,name='addip'),
    path('hello/',views.hello,name='hello'),
    path('oplog/',views.oplog,name='oplog'),
]
