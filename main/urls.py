
from django.urls import path 
from  . import views as v

urlpatterns = [
    path("",v.home , name="home"),
    
    #projects filter
    path("filter_projects/",v.filter_projects),
    
    path("send_email/",v.send_mail),
    
    #blogger filter
    path("blog/",v.blog , name="blog"),
    path("filter_blogs/",v.filter_blogs),
    path("blog/<str:pk>/",v.blog_detail , name="blog_detail"),
    #blog api
    path("api/blog_list/",v.list_all_blog , name="blog_list"),
    path("api/create_blog/", v.create_blog , name="create_blog"),
]
