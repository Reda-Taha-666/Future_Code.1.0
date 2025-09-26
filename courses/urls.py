from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.courses, name='courses'),
#     path('<slug:slug>/', views.course_detail, name='course_detail'),


# ]


urlpatterns = [
    path('', views.courses, name='courses'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),

    path("course/<int:course_id>/start/", views.start_course, name="start_course"),
    path("course/<int:course_id>/lesson/<int:lesson_id>/", views.start_course, name="lesson_detail"),
]


