
from django.urls import path 
from  . import views as v

urlpatterns = [
    path("",v.home , name="home"),
    path("filter_projects/",v.filter_projects),
    path("send_email/",v.send_mail),
    path("blog/",v.blog , name="blog"),
]
