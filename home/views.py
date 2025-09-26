from django.shortcuts import render
from courses.models import Course
from blog.models import Post

# Create your views here.
def home(request):
    # latest_courses = Course.objects.all().order_by('_id')[3]
    latest_courses = Course.objects.all().order_by('-id')[:3]
    latest_post = Post.objects.all().order_by('-id')[:3]

    return render (request , 'pages/index.html' , {'latest_courses':latest_courses , 'latest_post':latest_post})


def services(request):
    return render (request , 'pages/services.html')