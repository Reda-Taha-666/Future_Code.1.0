from django.shortcuts import render, get_object_or_404
from .models import Course ,Lesson
# Create your views here.
def courses(request):
    courses = Course.objects.all().order_by('-created_at')
    return render (request , 'pages/courses.html', {'courses': courses})

# def course_list(request):
#     courses = Course.objects.all()  # الترتيب هييجي من الـ model Meta
#     return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'page/course_detail.html', {'course': course})



def start_course(request, course_id, lesson_id=None):
    course = get_object_or_404(Course, id=course_id)
    lessons = course.lessons.order_by("order")
    if lesson_id:
        lesson = get_object_or_404(Lesson, id=lesson_id, course=course)
    else:
        lesson = lessons.first()  # يبدأ من أول درس

    return render(request, "page/start_course.html", {
        "course": course,
        "lessons": lessons,
        "lesson": lesson,
    })





# def course_detail(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     lessons = course.lessons.all()
#     return render(request, "page/course_detail.html", {
#         "course": course,
#         "lessons": lessons
#     })
