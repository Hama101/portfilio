from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from .models import *
from django.conf import settings
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BlogSerializer

MY_EMAIL = "hamdi_mohamed2018@hotmail.com"


def home(request):
    coding_skills = Skill.objects.all().filter(_type = "coding")
    other_skills = Skill.objects.all().filter(_type = "other")

    educations = Education.objects.all().filter().order_by("-year")
    experiences = Experience.objects.all().order_by("-year")

    projects = Project.objects.all()

    testimonials = Testimonial.objects.all()
    blogs = Blog.objects.all()

    if request.method =="POST":
        mail = Mail()
        mail.name = request.POST.get("name")
        mail.email = request.POST.get("email")
        mail.subject = request.POST.get("subject")
        mail.body = request.POST.get("body")
        mail.save()

    context = {
        "coding_skills":coding_skills,
        "other_skills" : other_skills ,
        "educations" : educations,
        "experiences" : experiences,
        "projects" : projects,
        "testimonials":testimonials,
        "blogs":blogs,
    }
    return render(request , "index.html" , context)


def filter_projects(request):
    _type = request.GET.get('type')
    if _type == "*":
        projects = Project.objects.all()
    else:
        projects = Project.objects.all().filter(_type__icontains=_type)

    t = render_to_string('projects.html',{"projects":projects})
    data = {
        "data":t
    }

    return JsonResponse(data)


def send_mail(request):
    send_mail(
            request.GET.get("subject"),
            f'{request.GET.get("email")}send : /n {request.GET.get("message")}',
            settings.EMAIL_HOST_USER,
            [MY_EMAIL],
            fail_silently=False,
            )
    return JsonResponse({"send":"send"})


def blog(request):
    blogs = Blog.objects.all()
    context = {
        "blogs" : blogs,
    }
    return render(request , "blog.html" , context)


def filter_blogs(request):
    _type = request.GET.get('type')
    if _type == "*":
        blogs = Blog.objects.all()
    else:
        blogs = Blog.objects.all().filter(_type__icontains=_type)

    t = render_to_string('blogs.html',{"blogs":blogs})
    data = {
        "data":t
    }

    return JsonResponse(data)


def blog_detail(request , pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        "blog":blog
    }
    return render(request , "blog_detail.html" , context)



@api_view(["POST"])
#create a new blog using serializers
def create_blog(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["GET"])
#list all the blog objects using serializers
def list_all_blog(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs,many=True)
    return Response(serializer.data)