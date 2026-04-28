from django.shortcuts import render
from .models import Course
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to Klaw Courses")

def detail_view(request, name):
    return HttpResponse(f"This is course: {name}")

def course_list(request):
    courses = Course.objects.all()
    
    context = {
        'title': 'Available Courses',
        'user_name': 'Aghin',
        'courses': courses
    }

    return render(request, 'courses/course_list.html', context)